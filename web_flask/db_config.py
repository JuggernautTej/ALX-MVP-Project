#!/usr/bin/python3

from flask_sqlalchemy import SQLALCHEMY


db = SQLAlchemy()

def initialize_db(app):
    app.config.form_object('web_flask.config.Config')
    db.init_app(app)
    with app.app_context():
        db.create_all()

# import mysql.connector

# db = mysql.connnector.connect(
#     host="localhost",
#     user="mvp_user",
#     password="Olujimi1!",
#     database="tech_news"
# )
# cursor = db.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS tech_news")
# cursor.execute("USE tech_news")
# cursor.execute("""
#     CREATES TABLE IF NOT EXISTS headline_news_us (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         title VARCHAR(524),
#         author VARCHAR(255),
#         description TEXT,
#         url VARCHAR(255),
#         image_url VARCHAR(255),
#         published_at DATETIME
#         )
#     """)
# cursor.execute("""
#     CREATES TABLE IF NOT EXISTS tesla_news (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         title VARCHAR(524),
#         author VARCHAR(255),
#         description TEXT,
#         url VARCHAR(255),
#         image_url VARCHAR(255),
#         published_at DATETIME
#         )
#     """)
# cursor.execute("""
#     CREATES TABLE IF NOT EXISTS apple_news (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         title VARCHAR(524),
#         author VARCHAR(255),
#         description TEXT,
#         url VARCHAR(255),
#         image_url VARCHAR(255),
#         published_at DATETIME
#         )
#     """)