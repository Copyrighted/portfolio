import datetime, bcrypt, uuid
from flask import render_template, redirect, url_for, request, flash, session
from werkzeug.urls import url_parse
from webapp import app, db
from webapp.forms import PostForm, LoginForm, DeleteForm, EditPostForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from webapp.models import User, Post

@app.route('/', methods=['GET'])
def render_main():
    return render_template('index.html')

@app.route('/projects', methods=['GET'])
def render_notes():
    post_list = Post.retrieve_posts()
    posts = []
    for post in post_list:
        posts.append("<a href='http://localhost:5000{url}' style='color:black;'><b>{title}</b></a>".format(url=url_for("get_content",id=post[0]),title = post[1]))
    return render_template('projects.html', posts=posts)


@app.route('/publish_post', methods=['GET', 'POST'])
@login_required
def render_publish():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(id=int(str(uuid.uuid4().int)[:16]),author=session["username"], body=form.post.data,timestamp=datetime.datetime.now().date(), title = form.title.data, user_id=session.get("_user_id"))
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('render_notes'))
    return render_template('publish_post.html', form=form)

@app.route('/edit/<string:id>', methods=['GET'])
@login_required
def render_edit(id):
    form = EditPostForm()
    post = Post.retrieve_post(id)
    return render_template('edit_post.html', form=form, post_title=post[0], post_content=post[1], id=id)

@app.route('/submit_edit/<string:id>', methods=['POST'])
@login_required
def edit_post(id):
    form = EditPostForm()
    if form.validate_on_submit():
        post = Post.query.filter_by(id=id)\
            .update(dict(title=form.title.data, body=form.post.data, timestamp=datetime.datetime.now().date()))
        db.session.commit()
        return redirect(url_for("render_options"))
    return redirect(url_for("render_main"))


@app.route('/delete/<string:id>', methods=['POST'])
@login_required
def delete_post(id):
    form = DeleteForm()
    if form.validate_on_submit():
        post = Post.query.get(int(id))
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('render_options'))

@app.route('/dashboard', methods=['GET'])
@login_required
def render_options():
    posts = Post.retrieve_posts()
    delete_form = DeleteForm()
    return render_template('dashboard.html', posts=posts, delete_form=delete_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
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
        session["username"]=form.username.data
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('render_notes'))

@app.route('/post/<int:id>/', methods=['GET'])
def get_content(id):
    post_info = Post.retrieve_post(id)
    print(post_info)
    return render_template("post_content.html", post_title=post_info[0], post_body=post_info[1], post_timestamp=post_info[2].date())

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # user = User(username=form.username.data, email=form.email.data)
        # user.set_password(form.password.data)
        # db.session.add(user)
        # db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        flash('Sorry, registration is currently blocked right now.')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)

@app.errorhandler(403)
def page_not_found(e):
    # note that we set the 403 status explicitly
    return render_template('/errors/403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('/errors/404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 500 status explicitly
    return render_template('/errors/500.html'), 500