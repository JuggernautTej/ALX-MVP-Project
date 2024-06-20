#!/usr/bin/python3
"""This script fetches data via the newsapi.org API
and stores it in the MySQL databse using SQLAlchemy"""


import requests
from datetime import datetime
from web_flask.db_config import db
from web_flask.models import NewsArticle
from flask import current_app as app

def fetch_store_news(category):
    url = 'https://newsapi.org/v2/top-headlines' if category == 'technology' else 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': app.config['NEWS_API_KEY'],
        'pageSize': 10 if category == 'technology' else 5,
        'category': 'technology' if category == 'technology' else None,
        'q': None if category == 'technology' else category,
        'country': 'us' if category == 'technology' else None,
        'from': '2024-06-17' if category != 'technology' else None, 
        'language':'en'
        }
    
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])

    for article in articles:
        news_article = NewsArticle(
            title=article['title'],
            author=article.get('author'),
            description=article['description'],
            url=article['url'],
            image_url=article.get('urlToImage'),
            published_at=datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
            category=category
        )
        db.session.add(news_article)
    db.session.commit()

def fetch_headlines():
    fetch_store_news('technology')

def fetch_tesla_news():
    fetch_store_news('tesla')

def fetch_apple_news():
    fetch_store_news('apple')