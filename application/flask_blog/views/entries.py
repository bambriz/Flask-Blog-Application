from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry
from flask_blog.models.comments import Comment
from flask_blog.models.users import User
from flask_login import current_user


@app.route('/')
def show_entries():
	if not current_user.is_authenticated:
		return redirect(url_for('welcome'))
	entries = Entry.query.order_by(Entry.id.desc()).all()
	return render_template('entries/index.html', entries=entries)

@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not current_user.is_authenticated:
        return redirect(url_for('welcome'))
    return render_template('entries/new.html')

@app.route('/entries', methods=['POST'])
def add_entry():
	if not current_user.is_authenticated:
		return redirect(url_for('welcome'))
	entry = Entry(
		title=request.form['title'],
		imglnk=request.form['imglnk'],
		text=request.form['text']
	)
	db.session.add(entry)
	db.session.commit()
	flash('A new article has been created.')
	return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
	if not current_user.is_authenticated:
		return redirect(url_for('welcome'))
	entry = Entry.query.get(id)
	
	comments = Comment.query.filter_by(parentpostID = entry.id).order_by(Comment.path)
	return render_template('entries/show.html', entry=entry, comments=comments)
@app.route('/entries/<int:id>', methods=['POST'])
def new_reply(id,commentID=None):
	if "replytext" in request.form:
			text = request.form['replytext']
			author = current_user.username
			parentpostID = id
			parent_id = request.args['commentID']
			new_comment = Comment(text=text,author=author,parentpostID=parentpostID,parent_id=parent_id)
			new_comment.save()
	return redirect(url_for('show_entry',id=id))
@app.route('/entries/<int:id>', methods=['POST'])
def new_comment(id):
	if "commtext" in request.form:
		text = request.form['commenttext']
		author = current_user.username
		parentpostID = id
		new_comment = Comment(text=text,author=author,parentpostID=parentpostID)
		new_comment.save()
	return redirect(url_for('show_entry',id=id))
	