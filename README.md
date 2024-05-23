# Extracting Material Contracts via Edgar Full Text Search Parser

This project contains a script that searches the Edgar database for specific filings, parses the results, and outputs the download link and details into a pandas DataFrame. The download links can be used to download material contracts from these filings via BeautifulSoup.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Overview

The script helps in extracting material contracts from the Edgar database by searching for specific filings, parsing the results, and compiling the data into a CSV file. This can be particularly useful for financial analysts, researchers, and legal professionals.

## Features

- Searches Edgar database for specified filings
- Parses filing details
- Outputs results to a CSV file
- Generates download links for material contracts

## Setup

### Prerequisites

- Python 3.x
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- Required Python libraries:
  - pandas
  - selenium
  - BeautifulSoup4

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/edgar-full-text-search-parser.git
   cd edgar-full-text-search-parser
