#!/usr/bin/python3
"""This script defines the route for the Flask RESTful
app"""

import requests
from flask import send_from_directory, current_app as app
from flask_restful import Resource, Api


def fetch_news(category):
    url = 'https://newsapi.org/v2/top-headlines' if category == 'technology' else 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': app.config['NEWS_API_KEY'],
        'pageSize': 10 if category == 'technology' else 5,
        'category': 'technology' if category == 'technology' else None,
        'q': None if category == 'technology' else category,
        'country': 'us' if category == 'technology' else None,
        'from': '2024-06-30' if category != 'technology' else None, 
        'language':'en'
        }
    
    response = requests.get(url, params=params)
    return response.json().get('articles', [])

class News(Resource):
    def get(self, category):
        articles = fetch_news(category)
        return {'news': articles}
    
def initialize_routes(api):
    api.add_resource(News, '/news/<string:category>')

def initialize_static_routes(app):
    @app.route('/')
    def index():
        return send_from_directory('..', 'index.html')
    
    @app.route('/<path:path>')
    def static_proxy(path):
        return send_from_directory('..', path)
