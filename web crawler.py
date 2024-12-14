import requests
from bs4 import BeautifulSoup
def web_crawler():
    url = input("Enter URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    for link in links:
        print(link['href'])
web_crawler()
