from getpass import getpass
from webapp import app, db
import bcrypt
from webapp.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

def main():
    with app.app_context():
        db.metadata.create_all(db.engine)
        if User.query.count() != 0:
            print('A user already exists! Create another? (y/n): ')
            create = input()
            if create == 'n':
                return
        print('Please enter username: ')
        username = input()
        print('Enter email address: ')
        email = input()
        print("Enter Password")
        password = getpass()
        print("Enter password again")
        assert password == getpass('Password (again):')
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        user = User(username=username, email=email, password_hash=bcrypt.hashpw(password, salt))
        db.session.add(user)
        db.session.commit()
        print('User successfully added')


if __name__ == '__main__':
    #main()
    app.run(host="0.0.0.0", port=5000)
