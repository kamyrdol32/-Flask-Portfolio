class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ""

    SESSION_COOKIE_SECURE = False

    # MAIL
    MAIL_SERVER = ""
    MAIL_PORT = 465
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True