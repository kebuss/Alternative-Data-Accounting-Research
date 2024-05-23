# -*- coding: utf-8 -*-
"""
Extracting 10-K Exhibits via Edgar Full Text Search Parser
=============================
This script searches the Edgar database for specific filings, parses the results,
and outputs the download link and details into a pandas DataFrame. The download links can be used to scrape
e.g. material contracts from these filings, and there are lots of beautiful existing scraping tutorials to do that.

Author: Keno Buß
Date: 23.05.2024
"""

import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# INPUT PARAMETERS
search_term = "Loan Agreement ex 10"
form = "10-K"
start_date = '2024-02-10'
end_date = '2024-02-15'
max_page = 3
# Insert page length to control the time, depends on the number of expected hits 
# Maximum of 10 pages for the full text search (~10*130 Results maximum), although more results exists, therefore daily pull

# Function to format search terms and dates
def format_search_term(term):
    return term.replace(" ", "%2520")

def format_dates(start_date, end_date):
    dates = pd.date_range(start_date, end_date, freq='D')
    return dates.strftime('%Y-%m-%d').tolist()

# Set up the web driver
driver = webdriver.Chrome()

# Format search term and dates
search_term = format_search_term(search_term)
dates = format_dates(start_date, end_date)
URL_BASIS = "https://www.sec.gov/Archives/edgar/data/"

# Initialize lists for DataFrame
file_date = []
reporting_date = []
filing_entity = []
located = []
incorporated = []
ciks = []
accessions = []
names = []
links = []

# Loop through each date and page to collect data
for date in dates:
    edgar_url = f"https://www.sec.gov/edgar/search/#/q={search_term}&dateRange=custom&category=custom&startdt={date}&enddt={date}&forms={form}"
    for p in range(1, max_page + 1):
        url = f"{edgar_url}=page={p}"
        driver.get(url)
        time.sleep(3)  # Wait for the page to load
        soup = BeautifulSoup(driver.page_source, 'lxml')
        
        # Parse filing data
        for fd in soup.findAll('td', class_="filed"):
            file_date.append(fd.text.strip())
        for rd in soup.findAll('td', class_="enddate"):
            reporting_date.append(rd.text.strip())
        for fe in soup.findAll('td', class_="entity-name"):
            filing_entity.append(fe.text.strip())
        for en in soup.findAll('td', class_="biz-location"):
            located.append(en.text.strip())
        for ec in soup.findAll('td', class_="incorporated d-none"):
            incorporated.append(ec.text.strip())
        for cik in soup.findAll('td', class_="cik d-none"):
            ciks.append(cik.text.strip())
        for acc in soup.findAll('a', class_="preview-file"):
            adsh = acc['data-adsh']
            accessions.append(adsh.replace("-", ""))
        for nam in soup.findAll('a', class_="preview-file"):
            names.append(nam['data-file-name'])
        
# Construct download links
for i in range(len(ciks)):
    document_link = f"{URL_BASIS}{ciks[i]}/{accessions[i]}/{names[i]}"
    links.append(document_link)

# Create DataFrame with collected data
df_info = pd.DataFrame({
    "download_link": links,
    "filing_date": file_date,
    "reporting_date": reporting_date,
    "entity": filing_entity,
    "location": located,
    "incorporation": incorporated,
    "CIK": ciks,
    "data_name": names,
    "accession_number": accessions
})

# Drop duplicates
df_info = df_info.drop_duplicates()

# Close the web driver
driver.quit()
