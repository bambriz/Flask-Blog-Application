#flask_blog/views.py
from flask import request, redirect, url_for, render_template, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_blog import app
from flask_blog import db
from flask_blog.models.users import User
from flask_login import login_user, login_required, current_user, logout_user
import datetime 
from flask_blog.models.entries import Entry
from flask_blog.models.comments import Comment


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		userName = request.form.get('username')
		password = request.form.get('password')
		# passwordConfirm = request.form.get('passwordconfirm')

		user = User.query.filter_by(username=userName).first()
		if user:
			flash('Username is already taken')
			return redirect(url_for('signup'))
		if len(password) < 8:
			flash('Password must be at least 8 characters long')
			return redirect(url_for('signup'))
		new_user =User(username=userName,password=generate_password_hash(password, method='sha256'))

		db.session.add(new_user)
		db.session.commit()
		flash('Account Creation Successful')
		return redirect(url_for('login'))
	return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		remember = True if request.form.get('remember') else False

		user = user = User.query.filter_by(username=username).first()

		if not user:
			flash('User name is different')
		elif not check_password_hash(user.password, password):
			flash('Password is different')
		else:
			login_user(user, remember=remember)
			session['logged_in'] = True
			flash('Login successful')
			return redirect(url_for('show_entries'))
	return render_template('login.html')

@app.route('/logout')
def logout():
	logout_user()
	flash('Logged Out')
	return redirect(url_for('welcome'))

@app.route('/profile')
def profile():
	if not session.get('logged_in'):
		return redirect(url_for('welcome'))
	entries = Entry.query.filter_by(created_by=current_user.username)
	comments = Comment.query.filter_by(author=current_user.username)
	return render_template('profile.html',name=current_user.username,entries=entries, comments=comments)

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')