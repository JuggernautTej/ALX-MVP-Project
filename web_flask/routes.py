#!/usr/bin/python3
"""This script defines the route for the Flask RESTful
app"""


from flask_restful import Resource, Api
from models import NewsArticle
#from web_flask.db_config import db


class News(Resource):
    def get(self, category):
        articles = NewsArticle.query.filter_by(category=category).all()
        return {'news': [article.to_dict() for article in articles]}
    
def initialize_routes(api):
    api.add_resource(News, '/news/<string:category>')

