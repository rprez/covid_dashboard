"""Application config class."""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    DATABASE_URI = os.environ.get('MONGODB_URI')
    DATABASE_NS = os.environ.get('MONGODB_NS')

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'
    ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"
    ENV = 'development'

class TestingConfig(Config):
    TESTING = True
    ENV = 'testing'
