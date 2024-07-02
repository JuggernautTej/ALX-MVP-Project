#!/usr/bin/python3
"""This script sets up the SQLAlchemy database connection
and initializes the database"""

from config import Config
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects import registry
# import mysql.connector

# Manually register the MySQL dialect
# registry.register("mysql.mysqlconnector", "mysql.connector", "MySQLDialect_mysqlconnector")

db = SQLAlchemy()

# print(dir(db))

def initialize_db(app):
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
