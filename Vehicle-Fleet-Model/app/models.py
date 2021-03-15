from flask_sqlalchemy import SQLAlchemy
import datetime
import pytz

time_zone = pytz.timezone('America/Mexico_City')

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    phone_number = db.Column(db.String(10))
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now(time_zone))


class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now(time_zone))


class Model(db.Model):
    __tablename__ = 'model'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now(time_zone))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(100))
    model_year = db.Column(db.String(4))
    description = db.Column(db.String(256))
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now(time_zone))
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))


class VehicleAssignment(db.Model):
    __tablename__ = 'vehicle_assignment'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, default=datetime.datetime.now(time_zone))
    expiration_date = db.Column(db.DateTime, default=datetime.datetime.now(time_zone))
    active = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))