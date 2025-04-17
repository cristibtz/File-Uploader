import os

class BaseConfig(object):
    DEBUG = os.environ['DEBUG']
    USERNAME = os.environ['USERNAME']
    SECRET_KEY = os.environ['SECRET_KEY']
    DB_NAME = os.environ['POSTGRES_DB']
    DB_USER = os.environ['POSTGRES_USER']
    DB_PASS = os.environ['POSTGRES_PASSWORD']
    DB_PORT = os.environ['DATABASE_PORT']
    DB_HOST = os.environ['DATABASE_HOST']
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
pass