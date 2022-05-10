import pandas as pd
import acquire_codeup_blog as acb
import acquire_news_articles as ana
import os

## COMMENT ALL

def get_blog_articles():
    urls = acb.get_blog_urls()
    articles = []
    
    for url in urls:
        articles.append(acb.get_article_info(url))
    df = pd.DataFrame(articles)
    return df

# REASSESS

def get_news_articles(use_cache=True):
    if os.path.exists('news_articles.json') and use_cache:
        return pd.read_json('news_articles.json')

    categories = ['business', 'sports', 'technology', 'entertainment']

    articles = []

    for category in categories:
        print(f'Getting {category} articles')
        articles.extend(ana.parse_news_category(category))

    df = pd.DataFrame(articles)
    df.to_json('news_articles.json', orient='records')
    return df