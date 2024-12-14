import pyshorteners
def url_shortener():
    url = input("Enter URL: ")
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    print("Short URL:", short_url)
url_shortener()
