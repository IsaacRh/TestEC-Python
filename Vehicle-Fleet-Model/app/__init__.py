from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)

    # set config to app
    app.config.from_object(Config)
    return app