from webapp import db

class user(db.Model):
    id = db.column(db.Integer, primary_key = True)
    username = db.column(db.String(64), index= True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(256))


    #repr method tells  Python how to print objects of his class
    def __repr__(self):
        return '<user {}>'.format(self.username)

#todo create blogpost class for db