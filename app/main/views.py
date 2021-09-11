from flask import render_template
from . import main
from ..requests import get_source, get_articles, get_articles_from_source, get_articles_depending_on_category


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news sources
    sources = get_source()
    # get articles from bbc-news
    bbc_news = get_articles_from_source('bbc-news', '8')
    # get articles from al-jazeera-english
    aljazeera_english = get_articles_from_source('al-jazeera-english', '8')
    bbc_home_picture = get_articles_from_source('bbc-news', '1')
    cnn = get_articles_from_source('cnn', '2')
    google = get_articles_from_source('google-news', '2')
    title = 'Home - Welcome to The best Hot News in the world'
    return render_template('index.html',
                           title=title,
                           sources=sources,
                           bbc_news=bbc_news,
                           aljazeera_english=aljazeera_english,
                           bbc_home_picture=bbc_home_picture,
                           cnn=cnn,
                           google=google
                           )


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


@main.route('/business')
def business():
    '''
    View business page function that returns the business page and its data
    '''
    business = get_articles_depending_on_category('business')
    title = 'Business - Welcome to The best Hot News in the world'
    return render_template('business.html',
                           title=title,
                           business=business
                           )


@main.route('/sports')
def sports():
    '''
    View sports page function that returns the sports page and its data
    '''
    sports = get_articles_depending_on_category('sports')
    title = 'Sports - Welcome to The best Hot News in the world'
    return render_template('sports.html',
                           title=title,
                           sports=sports
                           )


@main.route('/entertainment')
def entertainment():
    '''
    View entertainment page function that returns the entertainment page and its data
    '''
    entertainment = get_articles_depending_on_category('entertainment')
    title = 'Entertainment - Welcome to The best Hot News in the world'
    return render_template('entertainment.html',
                           title=title,
                           entertainment=entertainment
                           )


@main.route('/technology')
def technology():
    '''
    View technology page function that returns the technology page and its data
    '''
    technology = get_articles_depending_on_category('technology')
    title = 'Technology - Welcome to The best Hot News in the world'
    return render_template('technology.html',
                           title=title,
                           technology=technology
                           )


@main.route('/health')
def health():
    '''
    View health page function that returns the health page and its data
    '''
    health = get_articles_depending_on_category('health')
    title = 'Health - Welcome to The best Hot News in the world'
    return render_template('health.html',
                           title=title,
                           health=health
                           )


@main.route('/science')
def science():
    '''
    View science page function that returns the science page and its data
    '''
    science = get_articles_depending_on_category('science')
    title = 'Science - Welcome to The best Hot News in the world'
    return render_template('science.html',
                           title=title,
                           science=science
                           )
