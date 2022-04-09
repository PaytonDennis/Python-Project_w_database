#Flask application
from flask import Flask

#create app function and set key
def create_app():
    app = Flask(__name__)
    
    #data incrption
    app.config['SECRET_KEY'] = 'awdkjahwdkhadu'
    
    return app