from flask import Blueprint, render_template, request

#blueprint of application with roots

#blueprint for flask application
auth = Blueprint('auth', __name__)

#define login
@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="Payton", user ="Payton")

#define log out
@auth.route('/logout')
def loutout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            #add user to database
            pass
        
    return render_template("sign_up.html")
