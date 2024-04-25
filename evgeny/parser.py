
# scraper.py
import requests
from bs4 import BeautifulSoup


def parser(url: str = None) -> dict:
    response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find_all('blockquote', class_='abstract mathjax')
    
    
    links = []
    for n, i in enumerate(text, start=1):
        link = i.find('a')
        # print(link)
        if link:
            links.append(str(link).split("href=")[1].split(" rel")[0].split('\"')[1])
        # itemPrice = i.find('h5').text
        # print(f'{n}:  {itemPrice} за {itemName}')
        # print(itemName)
        
    # quotes = soup.find_all('span', class_='descriptor')
    title = str(soup.find_all('h1', class_='title mathjax')).split("</span>")[1].split("</h1>")[0]
    
    
    return {"title": title, "text": text, "links": links}


def parser_links(text: str = "") -> list[str]:
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