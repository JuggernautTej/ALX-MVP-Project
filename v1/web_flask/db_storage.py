#!/usr/bin/python3

import mysql.connector
import requests
from datetime import datetime
from mysql.connector import Error

db_host="localhost"
db_user="mvp_user"
db_pword="Olujimi1!"
db_name="tech_news"

def fetch_headlines():
    url = "https://newsapi.org/v2/top-headlines"
    API_KEY = "f26b66c5c8cd4b8c92b24c71f0bcf4f4"
    params = {'apiKey': API_KEY, 'pageSize': 10,
        'category': 'technology', 'country': 'us'}
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])

    try:
        connection = mysql.connector.connect(
            host=db_host, user=db_user,
            password=db_pword, database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
        for article in articles:
            cursor.execute("""
                INSERT INTO headline_news_us (title, author,
                description, url, image_url, published_at)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (article['title'], article['author'], article['description'], article['url'], article['urlToImage'], datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')))
        connection.commit()
        #print (f"Inserted {cursor.rowcount} articles into the database.")
    except Error as e:
        print (f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()   


def fetch_tesla_news():
    url = "https://newsapi.org/v2/everything"
    API_KEY = "f26b66c5c8cd4b8c92b24c71f0bcf4f4"
    params = {'apiKey': API_KEY, 'pageSize': 5,
        'q': 'tesla', 'from': '2024-06-17', 'sortBy': 'publishedAt', 'language': 'en'}
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])

    try:
        connection = mysql.connector.connect(
            host=db_host, user=db_user,
            password=db_pword, database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()    
        for article in articles:
            cursor.execute("""
                INSERT INTO tesla_news (title, author,
                description, url, image_url, published_at)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (article['title'], article['author'], article['description'], article['url'], article['urlToImage'], datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')))
            connection.commit()
    except Error as e:
        print (f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close() 

def fetch_apple_news():
    url = "https://newsapi.org/v2/everything"
    API_KEY = "f26b66c5c8cd4b8c92b24c71f0bcf4f4"
    params = {'apiKey': API_KEY, 'pageSize': 5,
        'q': 'apple', 'from': '2024-06-17', 'sortBy': 'publishedAt', 'language': 'en'}
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])

    try:
        connection = mysql.connector.connect(
            host=db_host, user=db_user,
            password=db_pword, database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
        for article in articles:
            cursor.execute("""
                INSERT INTO apple_news (title, author,
                description, url, image_url, published_at)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (article['title'], article['author'], article['description'], article['url'], article['urlToImage'], datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')))
            connection.commit()
    except Error as e:
        print (f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# fetch_news()
# fetch_tesla_news()
# fetch_apple_news()