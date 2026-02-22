"""Web Scraper — scrape data from a public website.

Example: Scrape quotes from https://quotes.toscrape.com/
"""

# TODO: pip install requests beautifulsoup4
# from bs4 import BeautifulSoup
# import requests


def fetch_page(url):
    """Fetch a web page and return the HTML content."""
    # TODO: Use requests.get() with error handling
    # Hint: response = requests.get(url)
    # Hint: response.raise_for_status()
    # Hint: return response.text
    pass


def parse_quotes(html):
    """Extract quotes and authors from HTML."""
    # TODO: Parse HTML with BeautifulSoup
    # Hint: soup = BeautifulSoup(html, "html.parser")
    # Hint: quotes = soup.find_all("div", class_="quote")
    # Hint: for q in quotes:
    #           text = q.find("span", class_="text").get_text()
    #           author = q.find("small", class_="author").get_text()
    return []


def save_results(quotes, filename="quotes.json"):
    """Save scraped quotes to a JSON file."""
    # TODO: Write quotes list to JSON file
    pass


def main():
    print("Web Scraper")
    print("TODO: Install dependencies: pip install requests beautifulsoup4")
    print("TODO: Implement fetch_page(), parse_quotes(), save_results()")

    # TODO: Uncomment and implement:
    # url = "https://quotes.toscrape.com/"
    # html = fetch_page(url)
    # if html:
    #     quotes = parse_quotes(html)
    #     print(f"Found {len(quotes)} quotes")
    #     save_results(quotes)


if __name__ == "__main__":
    main()
