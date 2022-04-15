from flask import Blueprint

#blueprint of application with roots

#blueprint for flask application
auth = Blueprint('auth', __name__)

#define login
@auth.route('/login')
def login():
    return "<p>Login</p>"

#define login
@auth.route('/logout')
def loutout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
