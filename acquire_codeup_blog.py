from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_blog_urls():  
    
    url = 'https://codeup.com/blog/'
    headers = {'user-agent': 'Innis Data Science Cohort'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    urls = [a.attrs['href'] for a in soup.select('a.more-link')]
    
    return urls

def get_article_info(url):

    headers = {'user-agent': 'Innis Data Science Cohort'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.select_one('h1.entry-title').text
    published = soup.select_one('.published').text
    content = soup.select_one('.entry-content').text.strip()

    return {'title': title, 'published': published, 'content': content}

