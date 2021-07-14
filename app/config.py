""" Configuration classes """

import os
from pymodm import connect

class Config(object):
    TESTING = False
    DEBUG = True
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    connect(f'mongodb://{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}/{os.getenv("MONGO_DATABASE_NAME")}')

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass