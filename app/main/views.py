from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_source, get_articles, get_articles_bbc, get_articles_cnn
# from ..models import Source, Article


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news sources
    sources = get_source()
    # get articles from bbc-news
    bbc_news = get_articles('bbc-news')
    # get articles from al-jazeera-english
    aljazeera_english = get_articles('al-jazeera-english')
    print(sources)
    bbc_home_picture = get_articles_bbc()
    print(bbc_home_picture)
    cnn = get_articles_cnn()
    title = 'Home - Welcome to The best News Highlighter'
    return render_template('index.html', title=title, sources=sources, bbc_news=bbc_news, aljazeera_english=aljazeera_english, bbc_home_picture=bbc_home_picture, cnn=cnn)


@main.route('/source/articles/<source_id>')
def articles(source_id):
    '''
    View articles page function that returns the articles page from a source
    '''
    # Getting articles based on the source id
    articles = get_articles(source_id)
    print(articles)
    title = f'{source_id}'

    return render_template('articles.html', title=title, articles=articles)
