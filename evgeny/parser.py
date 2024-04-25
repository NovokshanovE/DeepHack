
# scraper.py
import requests
from bs4 import BeautifulSoup


def parser(url: str = None):
    response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all('blockquote', class_='abstract mathjax')
    # quotes = soup.find_all('span', class_='descriptor')

    return quotes


def parser_links(text: str = ""):
    url = f"https://arxiv.org/search/?query={text}&searchtype=all&source=header"
    
    response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all('p', class_='list-title is-inline-block')
    res = []
    for n, i in enumerate(quotes, start=1):
        itemName = i.find('a')
        # itemPrice = i.find('h5').text
        # print(f'{n}:  {itemPrice} за {itemName}')
        # print(itemName)
        res.append(str(itemName)[str(itemName).index("\"")+1: str(itemName).rindex("\"")])
    # quotes = soup.find_all('span', class_='descriptor')

    return res