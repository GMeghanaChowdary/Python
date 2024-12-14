import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())

url = input
