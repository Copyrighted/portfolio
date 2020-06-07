import datetime, bcrypt, uuid
from flask import render_template, redirect, url_for, request, flash, session
from werkzeug.urls import url_parse
from webapp import app, db
from webapp.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from webapp.models import User, Post


@app.route('/', methods=['GET'])
def render_main():
    return render_template('index.html')

@app.route('/projects', methods=['GET'])
def render_notes():
    return render_template('projects.html')


@app.route('/options', methods=['GET', 'POST'])
@login_required
def render_options():
    form = PostForm()

    if form.is_submitted():
         print("submitted")
    # if not form.validate():
    #     print(form.validate())

    print("CSRF FORM HIDDEN TAG " + form.hidden_tag())
    print(session['csrf_token'])
    print(session)

    print(form.validate_on_submit())

    print(form.errors)


    if form.validate_on_submit():
        print(session)

        post = Post(id=int(str(uuid.uuid4().int)[:16]),author=session["username"], body=form.post.data,timestamp=datetime.datetime.utcnow(), title = None, user_id=session.get("_user_id"))
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('render_notes'))

    return render_template('options.html', form=form)

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
        session["username"]=form.username.data
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('render_notes'))

@app.route('/secret')
def secret():
    return "This is spoopy"