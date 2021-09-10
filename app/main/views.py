from flask import render_template
from ..requests import get_source, get_articles, get_articles_from_source_selected, get_articles_depending_on_category_of_the_source
from . import main


@main.route('/')
def index():
    '''
    Function that returns the index page 
    '''
    # Getting popular news sources
    sources = get_source()
    # get articles from bbc-news
    bbc_news = get_articles_from_source_selected('bbc-news', '8')
    # get articles from al-jazeera-english
    aljazeera = get_articles_from_source_selected('al-jazeera-english', '8')
    cnn_home = get_articles_from_source_selected('cnn', '1')
    bbc_news_home = get_articles_from_source_selected('bbc-news', '2')
    cbc_news = get_articles_from_source_selected('cbc-news', '2')
    title = 'Home - Welcome to News App '
    return render_template('index.html',
                           title=title,
                           bcc=bbc_news_home,
                           bbc_news=bbc_news,
                           cnn_home=cnn_home,
                           sources=sources,
                           cbc_news=cbc_news,
                           aljazeera=aljazeera,
                           )


@main.route('/news-source/articles/<source_id>')
def articles(source_id):
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles = get_articles(source_id)
    title = f'{source_id}'

    return render_template('articles.html', title=title, articles=articles)


@main.route('/science')
def science():
    '''
    View science page function that returns the science page and its data
    '''
    science = get_articles_depending_on_category_of_the_source('science')
    title = 'Science - Welcome to The best Hot News in the world'
    return render_template('science.html',
                           title=title,
                           science=science
                           )


@main.route('/business')
def business():
    '''
    View business page 
    '''
    business = get_articles_depending_on_category_of_the_source('business')
    title = 'Business - Welcome to The best Hot News in the world'
    return render_template('business.html',
                           title=title,
                           business=business
                           )


@main.route('/entertainment')
def entertainment():
    '''
    View entertainment page 
    '''
    entertainment = get_articles_depending_on_category_of_the_source(
        'entertainment')
    title = 'Entertainment - Welcome to The best Hot News in the world'
    return render_template('entertainment.html',
                           title=title,
                           entertainment=entertainment
                           )


@main.route('/sports')
def sports():
    '''
    View sports page 
    '''
    sports = get_articles_depending_on_category_of_the_source('sports')
    title = 'Sports - Welcome to The best Hot News in the world'
    return render_template('sports.html',
                           title=title,
                           sports=sports
                           )


@main.route('/health')
def health():
    '''
    View health page function that returns the health page and its data
    '''
    health = get_articles_depending_on_category_of_the_source('health')
    title = 'Health - Welcome to The best Hot News in the world'
    return render_template('health.html',
                           title=title,
                           health=health
                           )


@main.route('/technology')
def technology():
    '''
    View technology page function that returns the technology page and its data
    '''
    technology = get_articles_depending_on_category_of_the_source('technology')
    title = 'Technology - Welcome to The best Hot News in the world'
    return render_template('technology.html',
                           title=title,
                           technology=technology
                           )
