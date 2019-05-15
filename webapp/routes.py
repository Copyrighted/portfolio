from flask import render_template, redirect, url_for, request, flash
from webapp import app
from webapp.forms import LoginForm

@app.route('/', methods=['GET'])
def render_main():
    return render_template('main.html')

@app.route('/notes', methods=['GET'])
def render_notes():
    return render_template('notes.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        #todo implement redirect to posting page
        return redirect(url_for('main'))

    return render_template('login.html', title = 'Sign In', form = form)


@app.route('/secret')
def secret():
    return "This is spoopy"