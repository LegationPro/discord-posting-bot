import requests

def get_tweets(query):
    resp = requests.get(f"http://localhost:4050/tweets/{query}")
    return resp.json()
