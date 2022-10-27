class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "$#C#T4et32twg"

    SESSION_COOKIE_SECURE = False

    # MAIL
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USERNAME = "kamyrdol32test@gmail.com"
    MAIL_PASSWORD = "rzfdqcttrbsmhsvr"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True