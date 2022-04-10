#import from innit 
#runs flask application from webserver
from distutils.log import debug
from website.templates._init_ import create_app

app = create_app()

#if we run file execute line
if __name__ == '__main__':
    
    #start application, run webserver, when changes made rerun web server
    app.run(debug=True)