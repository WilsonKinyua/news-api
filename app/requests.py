import urllib.request
import json
from .models import Sources, Articles
import os
# import news api source url from config.py

# getting api key
api_key = 'e05ca232a09f4c6394d6716dbcde7fef'
# getting news base url
base_url_source = None
# getting news articles base url
base_url_articles = None


def configure_request(app):
    global api_key, base_url_source, base_url_articles
    base_url_source = app.config['NEWS_API_SOURCE_URL']
    base_url_articles = app.config['NEWS_API_ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']


def process_results_sources(source_list):
    '''
    Function that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        # country = source_item.get('country')

        source_object = Sources(
            id, name, description, url, category, language)
        source_results.append(source_object)

    return source_results


def process_results_articles(articles_list):
    '''
    Function that processes the articles result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns:
        articles_results: A list of articles objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            articles_object = Articles(
                author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(articles_object)

    return articles_results


def get_source():  # function to get the source
    '''
    Function that gets the json response to our url request
    '''
    # get api key from the config file
    # get_source_url = base_url_source.format('api_key')
    get_source_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key)
    print(get_source_url)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results_sources(source_results_list)

    return source_results


# get articles by source id
def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    # get_articles_url = base_url_articles.format(source_id, api_key)
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        source_id, api_key)
    # get_articles_url = base_url_articles.format(source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        # load the data into a json object
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)
    return articles_results  # return the results


# get news relating to specific source and page size

def get_articles_from_source(source, pageSize):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}&pageSize={}'.format(source,
                                                                                                      api_key, pageSize)
    # get_articles_url = base_url_articles.format(source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        # load the data into a json object
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)
    return articles_results  # return the results

# get news depending on category


def get_articles_depending_on_category(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(
        category, api_key)
    # get_articles_url = base_url_articles.format(source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        # load the data into a json object
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)
    return articles_results  # return the results
