from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_source, get_articles
# from ..models import Source, Article


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news sources
    sources = get_source()
    print(sources)
    title = 'Home - Welcome to The best News Highlighter'
    return render_template('index.html', title=title, sources=sources)

@main.route('/source/articles/<source_id>')
def articles(source_id):
    '''
    View articles page function that returns the articles page and its data
    '''
    # Getting articles based on the source id
    articles = get_articles(source_id)
    print(articles)
    title = f'{source_id}'

    return render_template('articles.html', title=title, articles=articles)