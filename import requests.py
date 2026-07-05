import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("span", class_="titleline")

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, start=1):
            title = headline.get_text(strip=True)
            print(f"{i}. {title}")
            file.write(f"{i}. {title}\n")

    print("\nHeadlines saved successfully in headlines.txt")

except requests.exceptions.RequestException as e:
    print("Error:", e)