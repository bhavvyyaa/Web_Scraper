import requests
from bs4 import BeautifulSoup
URL = "https://www.thehindu.com/"
OUTPUT_FILE = "headlines.txt"

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines_h1 = soup.find_all("h1", class_="title")
        headlines_h2 = soup.find_all("h2", class_="title")
        return headlines_h1 + headlines_h2

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

def save_headlines(headlines, filename):
    try:
        with open(filename,"w") as f:
            f.write("=============HEADLINES=============\n\n")
            if headlines:
                for headline in headlines:
                    text = headline.get_text(strip=True)
                    if text:
                        f.write(text + "\n\n")
                print(f"Headlines extracted and saved to {filename} successfully.")
            else:
                f.write("No headlines found.\n")
                print("No headlines found.")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

scraped_headlines = fetch_headlines(URL)
save_headlines(scraped_headlines, OUTPUT_FILE)
