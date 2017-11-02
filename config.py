import os

class Config(object):
    pass

class DevConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/foo.db'