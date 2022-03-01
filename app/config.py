import os


class BaseConfig:
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    PROJECT_NAME = 'Akos - Queue'
    PROJECT_URL = 'https://tryakos.com'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
