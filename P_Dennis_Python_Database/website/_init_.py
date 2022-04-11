#Flask application
from flask import Flask

#create app function and set key
def create_app():
    app = Flask(__name__)
    
    #data incrption
    app.config['SECRET_KEY'] = 'awdkjahwdkhadu'
    
   #import blueprints
    from .views import views
    from .auth import auth

 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app