from flask import Flask, request
from flask import render_template

# from flask import

app = Flask(__name__)


@app.route('/welcome', methods=["POST"])
def welcome():
    correct = "admin@gmail.com"
    if request.method == "POST":
        eml = request.form['email']
    if correct == eml:
        return "Welcome, " + eml
    # put application's code here
    else:
        return 'Welcome, Anonymous'


@app.route('/')
def login_function():
    return render_template("index.html", user="Test user")


if __name__ == '__main__':
    app.run()
