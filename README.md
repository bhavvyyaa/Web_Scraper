# The Hindu Headline Scraper

This is a simple Python script that scrapes the main headlines from *The Hindu*'s homepage and saves them into a text file named `headlines.txt`.

## Description

The script uses the `requests` library to fetch the HTML content of `https://www.thehindu.com/` and the `BeautifulSoup` library to parse it. It specifically looks for `<h1>` and `<h2>` tags that have a `class` attribute of "title", extracts the text from these tags, and writes them to a local file.

## Prerequisites

Before you can run this script, you need to have **Python 3** installed on your system. You will also need two Python libraries:
*   `requests`
*   `beautifulsoup4`

## Installation

**Install the required libraries** using pip. Open your terminal or command prompt and run the following command:
    ```bash
    pip install requests beautifulsoup4
    ```

## How to Use

1.  Make sure the script (e.g., `scraper.py`) is saved in your desired directory.
2.  Navigate to that directory in your terminal.
3.  Run the script using the following command:
    ```bash
    python scraper.py
    ```
4.  After the script finishes, a confirmation message will appear in the terminal: `Headlines extracted and saved to headlines.txt successfully`.

## Output

The script will generate a file named **`headlines.txt`** in the same directory. This file will contain the scraped headlines, formatted with a title and blank lines between each headline for readability.
