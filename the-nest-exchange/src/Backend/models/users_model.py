from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#Class based off of users table in db
class users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50),nullable = False )
    password_hash = db.Column(db.String(150),nullable = False)
    role = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    date_created = db.Column(db.Timestamp, nullable = False)
    last_login = db.Column(db.Timestamp)

    #Function that sets password and will hash it
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #Function that checks input password to password in db
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
