user_bd = 'root'
password_db = 'root'
host_db = 'localhost'
name_bd = 'vehicleFleet'
class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(user_bd, password_db, host_db, name_bd)
    SQLALCHEMY_TRACK_MODIFICATIONS = False