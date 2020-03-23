import bcrypt
from flask import render_template, redirect, url_for, request, flash, abort
from flask_admin.helpers import is_safe_url
from werkzeug.urls import url_parse

from webapp import app, db
from webapp.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from webapp.models import User

@app.route('/', methods=['GET'])
def render_main():
    return render_template('index.html')

@app.route('/projects', methods=['GET'])
def render_notes():
    return render_template('projects.html')


@app.route('/options', methods=['GET'])
@login_required
def render_options():
    return render_template('options.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        #todo implement posting/editing page
        return redirect(url_for('render_options'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not bcrypt.checkpw(form.password.data.encode('utf-8'), user.password_hash):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('render_options')
        flash('Logged in successfully')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('render_notes'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post 1'}
        ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/secret')
def secret():
    return "This is spoopy"