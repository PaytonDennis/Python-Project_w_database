#import from innit 
#runs flask application from webserver
from distutils.log import debug
from website import create_app

app = create_app()

#if we run file execute line
if __name__ == '_main_':
    
    #start application, run webserver, when changes made rerun web server
    app.run(debug=True)