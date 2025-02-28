import os
from sqlalchemy import create_engine #type: ignore
import urllib

class Config(object):
    SECRET_KEY='Clave nueva'
    SESSION_COOKIE_NAME=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False