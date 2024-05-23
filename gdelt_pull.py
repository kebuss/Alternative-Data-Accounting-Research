# -*- coding: utf-8 -*-
"""
GDELT Data Download and Analysis Script
=======================================
This script downloads and analyzes data from the GDELT (Global Database of Events, Language, and Tone) using version 2 of the GDELT API. 
All Credits to the amazing work of the GDELT Project: https://www.gdeltproject.org
The script performs the following steps:
1. Queries GDELT data for specified date ranges.
2. Filters the data to include only records based in the United States.
3. Retrieves the tone measure by GDELT.

Author: Keno Buß
Date: 23.05.2024
"""

import gdelt
import pandas as pd
import datetime

# INPUT PARAMETERS
start_date = datetime.date(2021, 3, 1)
end_date = datetime.date(2021, 3, 31)

# Initialize GDELT version 2 API
gdelt_api = gdelt.gdelt(version=2)

# Initialize a list to store data
request_dates = []
failed_requests = []
all_data = []

#Initialize Dates for Requests
date_range = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]
for single_date in date_range:
    request_dates.append(single_date.strftime('%Y') + ' ' + single_date.strftime('%b') + ' ' + single_date.strftime('%d'))

# Iterate through the list of request dates
for request_date in request_dates:
    try:
        # Query the GDELT API for the given date
        results = gdelt_api.Search(request_date, table='gkg')
        data_frame = pd.DataFrame(results)
        data_frame['date'] = request_date
        # Filter the data to include only records based in the United States
        us_data = data_frame[data_frame['Locations'].str.contains('United States|US', na=False)]
        # Drop duplicate records
        us_data = us_data.drop_duplicates(keep="last")
        # Append the filtered data to the list
        all_data.append(us_data)
    except ValueError:
        # Add the date to the list of failed requests if an error occurs
        failed_requests.append(request_date)

# Concatenate all the data into a single DataFrame
concatenated_data = pd.concat(all_data, ignore_index=True)
concatenated_data = concatenated_data.drop_duplicates()

# Select relevant columns for further analysis
selected_data = concatenated_data[['DATE', 'date', 'GKGRECORDID', 'SourceCommonName', 'Themes', 'Locations', 'V2Tone']]
tone_data = selected_data['V2Tone'].str.split(',', expand=True)
tone_data.columns = ['tone', "positive_score", "negative_score", "polarity_score", "activity_reference_density", "group_reference_density", "word_count"]
df_info = pd.concat([selected_data, tone_data], axis=1)

# Brief Explanation of tone data fields from the documentation (https://www.gdeltproject.org/data.html):
# Results a comma-delimited list of six core emotional dimensions, described in more detail below. Each is recorded as a single precision floating point number.
#   Tone. (floating point number) This is the average “tone” of the document as a whole. The score ranges from -100 (extremely negative) to +100 (extremely positive). Common values range between -10 and +10, with 0 indicating neutral. This is calculated as Positive Score minus Negative Score.
#       Note that both Positive Score and Negative Score are available separately below as well. A document with a Tone score close to zero may either have low emotional response or may have a Positive Score and Negative Score that are roughly equivalent to each other, such that they nullify each other.
#       These situations can be detected either through looking directly at the Positive Score and Negative Score variables or through the Polarity variable.
# * Positive Score. (floating point number) This is the percentage of all words in the article that were found to have a positive emotional connotation. Ranges from 0 to +100.
# * Negative Score. (floating point number) This is the percentage of all words in the article that were found to have a negative emotional connotation. Ranges from 0 to +100.
# * Polarity. (floating point number) This is the percentage of words that had matches in the tonal dictionary as an indicator of how emotionally polarized or charged the text is. If Polarity is high, but Tone is neutral, this suggests the text was highly emotionally charged, but had roughly equivalent numbers of positively and negatively charged emotional words.
# * Activity Reference Density. (floating point number) This is the percentage of words that were active words offering a very basic proxy of the overall “activeness” of the text compared with a clinically descriptive text.
# * Self/Group Reference Density. (floating point number) This is the percentage of all words in the article that are pronouns, capturing a combination of self-references and group-based discourse. News media material tends to have very low densities of such language, but this can be used to distinguish certain classes of news media and certain contexts.
# * Word Count. (integer) This is the total number of words in the document. This field was added in version 1.5 of the format.