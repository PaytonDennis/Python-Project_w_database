#import from innit 
#runs flask application from webserver
from distutils.log import debug
from website._init_ import create_app
import requests

app = create_app()

#if we run file execute line
if __name__ == '__main__':
    
    #start application, run web server, when changes made rerun web server
    #debug=True debugs server every time run
    app.run(debug=True)