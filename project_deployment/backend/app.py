#!/usr/bin/python3
"""This script initializes the Flask application"""

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes import initialize_routes, initialize_static_routes
from config import Config
import os

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config.from_object(Config)

initialize_routes(api)
initialize_static_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)
