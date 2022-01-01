from flask_blog import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	displayname = db.Column(db.String(100))
	biotext = db.Column(db.Text)
	created_at = db.Column(db.DateTime)
	profilepictureurl = db.Column(db.String(1000))

	def __init__(self,username, password, displayname=None, biotext=None, profilepictureurl=None):
		self.username = username
		self.password = password
		if profilepictureurl is None:
			self.profilepictureurl = 'https://www.pngitem.com/pimgs/m/84-844866_face-nose-black-facial-expression-person-smile-emotion.png'
		self.biotext = biotext
		self.created_at = datetime.utcnow()

	def __repr__(self):
		return '<Entry id:{} Username:{}'.format(self.id, self.username)