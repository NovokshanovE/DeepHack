
# scraper.py
import requests
from bs4 import BeautifulSoup


def parser(url: str = None):
    response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all('blockquote', class_='abstract mathjax')
    # quotes = soup.find_all('span', class_='descriptor')

    print(quotes)