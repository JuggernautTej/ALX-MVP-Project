#!/usr/bin/python3
"""This script initializes the Flask application"""

from flask import Flask
from flask_restful import Api
from routes import initialize_routes, initialize_static_routes
from config import Config
import os

app = Flask(__name__)
api = Api(app)

os.environ['NEWS_API_KEY'] = os.getenv('NEWS_API_KEY', 'f26b66c5c8cd4b8c92b24c71f0bcf4f4')

app.config.from_object(Config)

initialize_routes(api)
initialize_static_routes(app)

if __name__ == '__main__':
    app.run(debug=True)