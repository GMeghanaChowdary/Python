import requests
from bs4 import BeautifulSoup
def news_aggregator():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('a', class_='storylink')
    for headline in headlines:
        print(headline.text)
news_aggregator()
