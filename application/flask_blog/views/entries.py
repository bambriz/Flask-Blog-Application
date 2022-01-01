from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry
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
	return render_template('entries/show.html', entry=entry)

