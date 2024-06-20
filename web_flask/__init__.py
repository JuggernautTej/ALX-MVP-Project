#!/usr/bin/python3
"""This script initializes the Flask application"""

from flask import Flask
from flask_restful import Api
from web_flask.db_config import initialize_db
from web_flask.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config.from_object('web_flask.config.Config')

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)