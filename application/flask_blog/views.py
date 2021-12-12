#flask_blog/views.py
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route('/')
def hello_world():
  return render_template('entries/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			print('User name is different')
		elif request.form['password'] != app.config['PASSWORD']:
			print('Password is different')
		else:
			return redirect('/')
	return render_template('login.html')

@app.route('/logout')
def logout():
	return redirect('/')