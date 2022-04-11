from flask import Blueprint

#blueprint of application with roots

#blueprint for flask application
views = Blueprint('views', __name__)



#decorator with root
@views.route('/')
#runs home when you go to /
def home():
    return "<h1>Test</h1>"
