#!/usr/bin/python3

from flask_restful import Resource
from web_flask.config import api, app
import mysql.connector

db_host="localhost"
db_user="mvp_user"
db_pword="Olujimi1!"
db_name="tech_news"

class News(Resource):
    def get_headline(self):
        connection = mysql.connector.connect(
            host=db_host, user=db_user,
            password=db_pword, database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
        cursor.execute("SELECT * FROM headline_news_us")
        news = cursor.fetchall()
        return {'headlines': news}

api.add_resource(News, '/headlines')

if __name__ == '__main__':
    app.run(debug=True)