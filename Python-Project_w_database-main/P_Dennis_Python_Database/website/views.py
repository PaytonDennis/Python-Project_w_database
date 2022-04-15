from flask import Blueprint, render_template

#blueprint of application with roots

#blueprint for flask application
views = Blueprint('views', __name__)



#decorator with root
@views.route('/')
#runs home when you go to /
def home():
    return render_template("home.html")
