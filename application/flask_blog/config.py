#flask_blog/config.pow
import os
SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
USERNAME = os.getenv("usrnme")
PASSWORD = os.getenv("psswrd")
SECRET_KEY = os.getenv("secretKey")
DFLIMGLNK = 'https://www.pngitem.com/pimgs/m/84-844866_face-nose-black-facial-expression-person-smile-emotion.png'