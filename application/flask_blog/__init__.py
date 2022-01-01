from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views import views, entries

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from flask_blog.models.users import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
	return User.query.get(int(user_id))

# app.run(host='0.0.0.0', port=8080)