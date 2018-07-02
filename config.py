'''
CLASS:
    Config(): 모든 설정에 사용되는 공통 값을 포함하고 있다. 서로 다른 서브 클래스는 특정 설정에 대한 값을 정의한다.
    # 그 외 설정이 필요하다면 임의로 추가해도 무방하다.
    DevelopmentConfig(Config):
    TestingConfig(Config):
    ProductionConfig(Config):

Valiable:
    SQLALCHEMY_DATABASE_URI 변수는 세 개의 설정에 따라 각각 서로 다른 값으로 할당된다.
    # 각 애플리케이션이 서로 다른 데이터베이스와 다른 설정에서 동작하도록 해 준다.
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = os.environ.get('MAIL_SERVER', '587')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'ture').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ATHENA_MAIL_SUBJECT_PREFIX = '[ATHENA]'
    ATHENA_MAIN_SENDER = 'Athena Admin <gmj1197@gmail.com>'
    ATHENA_ADMIN = os.environ.get('ATHENA_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}