#!/usr/bin/python3
"""This script sets up the SQLAlchemy database connection
and initializes the database"""

from flask_sqlalchemy import SQLALCHEMY


db = SQLAlchemy()

def initialize_db(app):
    app.config.form_object('web_flask.config.Config')
    db.init_app(app)
    with app.app_context():
        db.create_all()
