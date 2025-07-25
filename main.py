from scraper.characters import scrape_characters
from scraper.utils import save_to_csv

if __name__ == "__main__":

    characters = scrape_characters()
    save_to_csv(characters, "data/characters.csv")
    print(f"Scraped {len(characters)} characters.")
