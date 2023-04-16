import requests

def getMoviesRequest(url):
    # Downloading imdb top 250 movie's data
    return requests.get(url).text
