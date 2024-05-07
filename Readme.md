# DAAD website Scraper

This application is designed to help you gather information about various programs in German universities listed on the DAAD.de website. It sends a GET request to the provided URL, parses the HTML response, and extracts the relevant information about each program. The extracted data is then stored in an Excel file for easy access and analysis.

## Features

- Extracts information about various programs in German universities from the DAAD.de website.
- Filters and organizes the data based on the user's preferences.
- Exports the data to an Excel file for easy access and analysis.

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python 3.
4. The script will send a GET request to the DAAD.de website, parse the HTML response, and extract the relevant information.
5. The extracted data will be stored in an Excel file in the same directory.

## Requirements

- Python 3
- `requests` library
- `beautifulsoup4` library
- `pandas` library

## Output

The output of this application is an Excel file containing the following information for each program:

- University Name
- Course Name
- Location
- Deadlines
- Link to the program's page on the DAAD.de website

## Disclaimer

This application is intended for educational purposes only. Please respect the terms of use of the DAAD.de website.