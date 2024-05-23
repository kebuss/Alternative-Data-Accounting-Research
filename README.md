# Alternative-Data-Accounting-Research

This repository is my introduction to GitHub and contains some scripts to gather alternative data, compared to the conventional data providers like Compustat or CRSP. I hope these scripts help (junior) researchers to pursue research questions and other interested readers.

## Table of Contents

- [Edgar Full Text Search Parser](#edgar-full-text-search-parser)
- [Global Database of Events, Language, and Tone (GDELT) Download](#global-database-of-events-language-and-tone-gdelt-download)

## Edgar Full Text Search Parser

The script helps in extracting 10-K exhibits (e.g. material contracts) from the Edgar database by searching for specific filings via the Edgar Full Text Search [Edgar database](https://www.sec.gov/edgar/search/#), parsing the results, and giving back the download links. The download links can be used to download e.g. material contracts from specific filings. There are lots of beautiful existing tutorials to scrape the text. The exhibits can be particularly useful for financial analysts, researchers, and legal professionals.

You can find the main script [here](https://github.com/kebuss/Alternative-Data-Accounting-Research/blob/main/edgar_search_parser.py).

## Global Database of Events, Language, and Tone (GDELT) Download

This script helps to download data from the GDELT (Global Database of Events, Language, and Tone) using version 2 of the GDELT API. The script facilitates the extraction of global news event data from the GDELT Project, a comprehensive database that monitors news media from around the world in real-time. By querying the GDELT version 2 API for specific date ranges, the script retrieves detailed event records and processes them to focus on events occurring in the United States. The Global Database of Events, Language, and Tone (GDELT) monitors broadcast, print, and web news from nearly every corner of the globe in over 100 languages, updating every 15 minutes to provide a real-time pulse of global events. This data can be particularly useful for researchers and professionals interested in global trends and events. For more information, visit the [GDELT Project website](https://www.gdeltproject.org).

You can find the main script [here](https://github.com/kebuss/Alternative-Data-Accounting-Research/blob/main/gdelt_data_download_analysis.py).
