#flask_blog/config.pow
import os
DEBUG = True
USERNAME = os.getenv("usrnme")
PASSWORD = os.getenv("psswrd")
SECRET_KEY = os.getenv("secretKey")