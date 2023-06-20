import requests
from config import newsapi_key

def fetch_news_headlines(query, api_key=newsapi_key, page_size=50):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": api_key,
        "pageSize": page_size,
        "language": "en",
        "sortBy": "relevance"
    }

    response = requests.get(url, params=params)
    news_data = response.json()

    headlines = [article['title'] for article in news_data['articles']]
    return headlines
