from decouple import config

class Config(object):
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    PORT = config('PORT', default=5000, cast=int)  # Add port setting here

class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
