
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('main.html')

@app.route('/notes')
def render_notes():
    return render_template('notes.html')

@app.route('/login')
def render_login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
