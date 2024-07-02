#!/usr/bin/python3
"""This script initializes the Flask application"""

from flask import Flask
from flask_restful import Api
from db_config import initialize_db
from routes import initialize_routes
from config import Config

app = Flask(__name__)
api = Api(app)

print(Config)

app.config.from_object(Config)

initialize_routes(api)
initialize_db(app)

if __name__ == '__main__':
    app.run(debug=True)