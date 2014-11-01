import os

class Config(object):
    DEBUG = False
    # If using a DB do something like this:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql+pg8000://readhub_user@localhost:5432/readhub_db')
    # if using WTF forms you'll want some thing like this below
    # CSRF_ENABLED = True
    # CSRF_SESSION_KEY = os.environ.get('SESSION_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(DevelopmentConfig):
    DEBUG = True
    TESTING = True
    # WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:test.db'