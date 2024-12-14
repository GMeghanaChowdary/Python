import requests
def news_aggregator():
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY'
    response = requests.get(url)
    articles = response.json()['articles']
    for article in articles:
        print(f"Title: {article['title']}\nDescription: {article['description']}\n")
news_aggregator()
