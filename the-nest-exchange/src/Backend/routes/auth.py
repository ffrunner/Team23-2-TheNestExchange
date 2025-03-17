from config.database_connect import connect_database
from flask import Blueprint, render_template, request, session, redirect, url_for
from models.users_model import users


auth = Blueprint('auth',__name__)

#Login function that searches db for email and password. 
@auth.route('/login', methods=["POST"])
def login():
    connection = connect_database()
    email = request.form['email']
    password = request.form['password']
    user = users.query.filter_by(email = email).first()
    #If correct email and password, begins session and takes user to dashboard
    if user and user.check_password(password):
        session['email'] = email
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
    user = users.query.filter_by(email=email).first()
    #If user is already in db, cannot be added again. 
    if user:
        connection.close()
        return "User already exists"
    else:
        #Else user can be added into db and will be taken to login screen after signing up
        new_user = users(email=email)
        new_user.set_password(password)
        connection.session.commit()
        session['email'] = email
        return redirect(url_for('login.js'))

#@auth.route('/change_password', methods = ['GET', 'POST'])
#def change_password():


#Function that logs user out and ends session
@auth.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login.js'))
