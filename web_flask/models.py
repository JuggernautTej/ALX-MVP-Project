#!/usr/bin/python3
"""This file defines the SQLAlchemy
models for the news articles"""
from web_flask.db_config import db
from datetime import datetime


class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(524))
    author = db.Column(db.String(255))
    description = db.Column(db.Text)
    url = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    published_at = db.Column(db.DateTime)
    category = db.Column(db.String(50))

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'url': self.url,
            'urlToImage': self.image_url,
            'publishedAt': self.published_at
        }