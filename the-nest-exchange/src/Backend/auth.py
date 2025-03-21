from database_connect import connect_database
from flask import Blueprint, render_template, request, session, redirect, url_for
from users_model import Users


auth = Blueprint('auth',__name__)

#Login function that searches db for email and password. 
@auth.route('/login', methods=["POST"])
def login():
    connection = connect_database()
    email = request.form['email']
    password = request.form['password']
    user = Users.query.filter_by(email = email).first()
    #If correct email and password, begins session and takes user to dashboard
    if user and user.check_password(password):
        session['email'] = email
        connection.close()
        return redirect(url_for('Dashboard.jsx'))
    else:
        connection.close()
        return "Invalid credentials"

#Sign up function that adds user to db 
@auth.route('/signup', methods=["POST"])
def sign_up():
    connection = connect_database()
    email = request.form['email']
    password = request.form['password']
    user = Users.query.filter_by(email=email).first()
    #If user is already in db, cannot be added again. 
    if user:
        connection.close()
        return "User already exists"
    else:
        #Else user can be added into db and will be taken to login screen after signing up
        new_user = Users(email=email)
        new_user.set_password(password)
        connection.session.add(new_user)
        connection.session.commit()
        connection.close()
        session['email'] = email
        return redirect(url_for('login.js'))

#Change password function that adds new hash password
@auth.route('/change_password', methods = ['GET', 'POST'])
def change_password():
    connection = connect_database()
    email = request.form['email']
    password = request.form['password']
    user = Users.query.filter_by(email = email).first()
    #If correct email and password, can change password
    if user and user.check_password(password):
         new_password = request.form(new_password)
         user.set_password(new_password)
         connection.session.commit()
         connection.close()
    else:
        connection.close()
        return "Invalid credentials"

#Function that logs user out and ends session
@auth.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login.js'))

