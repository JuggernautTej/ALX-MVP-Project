#!usr/bin/python3
"""This script contains the configuration settings for
accessing the APINEWS.org api
"""

import os


class Config:
    NEWS_API_KEY = os.getenv('NEWS_API_KEY', 'f26b66c5c8cd4b8c92b24c71f0bcf4f4')
    