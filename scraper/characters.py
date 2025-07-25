import requests
import time
from bs4 import BeautifulSoup
from config import CATEGORY_URL

def scrape_characters(limit=50):
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    }
    time.sleep(5)
    session = requests.Session()
    session.headers.update(headers)

    resp = session.get(CATEGORY_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    print(resp.status_code)

    characters = []
    items = soup.select("div.category-page__first-char")

    for link in items[:limit]:
        name = link.text.strip()
        href = link.get("href")
        if name and href:
            characters.append({
                "name": name,
                "url": CATEGORY_URL + href
            })

    return characters
