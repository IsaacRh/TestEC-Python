from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
if not database_exists(engine.url):
    create_database(engine.url)

def create_app():
    app = Flask(__name__)

    # set config to app
    app.config.from_object(Config)
    db = SQLAlchemy()
    db.init_app(app)
    return app