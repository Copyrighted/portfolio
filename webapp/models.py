from datetime import datetime
import bcrypt
from webapp import login, db, session
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def set_password(self, password):
        salt = bcrypt.gensalt()
        password = password.encode('utf-8')
        self.password_hash = bcrypt.hashpw(password, salt)

    def check_password(self, password):
        password = password.encode('utf-8')
        return bcrypt.checkpw(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    author = db.Column(db.String(50))
    body = db.Column(db.TEXT)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(256))

    @classmethod
    def retrieve_posts(cls):
        return session.query(Post.id, Post.title,Post.body,Post.timestamp).all()

    @classmethod
    def retrieve_post(cls, post_id):
        p = session.query(Post).get(post_id)
        return (p.title, p.body, p.timestamp)



    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    try:
        return User.query.get(id)
    except User.doesNotExist:
        return None