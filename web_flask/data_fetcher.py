#!/usr/bin/python3
"""Module to fetch data from the newsapi API"""

import requests
# import json
# from datetime import datetime

def fetch_data():
    """Function to fetch data from the newsapi API"""
    API_KEY = "f26b66c5c8cd4b8c92b24c71f0bcf4f4"
    url = "https://newsapi.org/v2/top-headlines"
    querystring = {
        "country": "us", "apiKey": API_KEY, "pageSize": 10,
        "category": "technology"
    }
    response = requests.get(url, params=querystring)
    data = response.json()
    articles = data["articles"]
    fetched_data = []
    for article in articles:
        fetched_data.append({
            "source": article["source"]["name"],
            "author": article["author"],
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "urlToImage": article["urlToImage"],
            "publishedAt": article["publishedAt"]
        })
    return fetched_data

def main():
    """Function to fetch and print data from the newsapi API"""
    data = fetch_data()
    for article in data:
        print(article)
        print()
