from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def render_main():
    return render_template('main.html')

@app.route('/notes', methods=['GET'])
def render_notes():
    return render_template('notes.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'far' and request.form['password'] == 'raf':
            return redirect(url_for('secret'))
        else:
            error = "잘못된 자격 증명"

    return render_template('login.html', error=error)

@app.route('/secret')
def secret():
    return "This is spoopy"


if __name__ == '__main__':
    app.run()
