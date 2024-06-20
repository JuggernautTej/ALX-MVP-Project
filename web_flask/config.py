#!usr/bin/python3
"""This script contains the configuration settings
for accessing the MySQL database and the Flask application"""
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://mvp_user:Olujimi1!@localhost:3306/tech_news'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    NEWS_API_KEY = os.getenv('NEWS_API_KEY', 'f26b66c5c8cd4b8c92b24c71f0bcf4f4')
    