from flask import Blueprint, render_template

#blueprint of application with roots

#blueprint for flask application
auth = Blueprint('auth', __name__)

#define login
@auth.route('/login')
def login():
    return render_template("login.html")

#define login
@auth.route('/logout')
def loutout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
