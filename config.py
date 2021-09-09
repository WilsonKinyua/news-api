import os


class Config:
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


config_map = {
    'development': DevelopmentConfig,
    'production': ProdConfig
}
