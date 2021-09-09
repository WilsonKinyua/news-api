from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_map

bootstrap = Bootstrap()  # Initialize the extension


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_map[config_name])
    config_map[config_name].init_app(app)
    # Initializing flask extensions
    bootstrap.init_app(app)

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
