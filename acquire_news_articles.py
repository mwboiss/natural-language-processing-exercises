from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import os

## REASSESS

def parse_news_card(card, category):
    output = {}

    output['category'] = category
    output['title'] = card.select_one('a.clickable').text.strip()

    card_content = card.select_one('.news-card-content')
    output['content'] = card_content.select_one('div').text

    author_and_time = card_content.select_one('.news-card-author-time')
    output['author'] = author_and_time.select_one('.author').text
    output['published'] = author_and_time.select_one('.time').attrs['content']

    return output

def parse_news_category(category):
    url = 'https://inshorts.com/en/read/' + category
    response = get(url)
    soup = BeautifulSoup(response.text)

    cards = soup.select('.news-card')
    articles = []

    for card in cards:
        articles.append(parse_news_card(card, category))

    return articles
