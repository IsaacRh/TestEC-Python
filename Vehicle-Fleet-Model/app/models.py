from flask_sqlalchemy import SQLAlchemy
import datetime
import pytz

time_zone = pytz.timezone('America/Mexico_City')

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    date_created = db.Column(db.DateTime, default=datetime.datetime.now(time_zone))