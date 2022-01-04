from flask_blog import db
from datetime import datetime
DFLIMGLNK = 'https://www.pngitem.com/pimgs/m/84-844866_face-nose-black-facial-expression-person-smile-emotion.png'

class Entry(db.Model):
	__tablename__ = 'entries'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), unique=True)
	imglnk = db.Column(db.String(1000))
	text = db.Column(db.Text)
	created_by = db.Column(db.String(32))
	created_at = db.Column(db.DateTime)

	def __init__(self, title=None, imglnk=None, text=None, created_by=None):
		self.title = title
		if imglnk is None:
			self.imglnk = 'https://www.pngitem.com/pimgs/m/84-844866_face-nose-black-facial-expression-person-smile-emotion.png'
		else:
			self.imglnk = imglnk
		self.text = text
		self.created_by = created_by
		self.created_at = datetime.utcnow()

	def __repr__(self):
		return '<Entry id:{} title:{} imglnk:{} text:{}'.format(self.id, self.title, self.imglnk, self.text)
	def getPassedTimeStamp(self):
		current = datetime.utcnow() -self.created_at
		minutes = divmod(current.total_seconds(), 60)
		return f'{int(minutes[0])} minutes and {int(minutes[1])} seconds'