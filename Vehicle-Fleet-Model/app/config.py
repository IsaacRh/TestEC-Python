class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/miniblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False