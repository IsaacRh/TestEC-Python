from flask import Flask
from .config import Config
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate
from .models import db

# CHECK the database in server, if not found, its created
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
if not database_exists(engine.url):
    create_database(engine.url)

migrate = Migrate()
def create_app():
    app = Flask(__name__)
    # set config to app
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    return app