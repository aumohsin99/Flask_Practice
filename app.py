from flask import Flask
from flask import render_template

# from flask import

app = Flask(__name__)


@app.route('/welcome', methods=["POST"])
def welcome():  # put application's code here
    return 'Welcome, '


@app.route('/')
def login_function():
    # return render_template(index.html)
    # return "Login Function tested!"
    return render_template("index.html", user="Test user")


if __name__ == '__main__':
    app.run()
