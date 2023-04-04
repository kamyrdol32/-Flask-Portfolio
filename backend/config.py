import os

# Flask
DEBUG = False
TESTING = False
SECRET_KEY = os.getenv("SECRET_KEY")
SESSION_COOKIE_SECURE = False

# MAIL
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_USE_TLS = False
MAIL_USE_SSL = True
