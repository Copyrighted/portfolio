from flask import render_template, redirect, url_for, request, flash
from webapp import app
from webapp.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from webapp.models import User

@app.route('/', methods=['GET'])
def render_main():
    return render_template('index.html')

@app.route('/notes', methods=['GET'])
def render_notes():
    return render_template('notes.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        #todo implement posting/editing page
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('render_login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('render_main'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/secret')
def secret():
    return "This is spoopy"