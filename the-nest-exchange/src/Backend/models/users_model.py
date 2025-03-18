from app import db
from werkzeug.security import generate_password_hash, check_password_hash

#Class based off of users table in db
class users(db.Model):
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
    
# Model for Activity Logs
class ActivityLog(db.Model):
    __tablename__ = "activity_log"
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

# Model for Listings
class Listings(db.Model):
    __tablename__ = "listings"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    claimed_by = db.Column(db.Integer, db.ForeignKey('users.id'))

# Model for Disputes
class Dispute(db.Model):
    __tablename__ = "disputes"
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    lister_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    claimer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    resolution_status = db.Column(db.String(50))  # e.g., 'resolved', 'pending', 'dismissed'

# Model for Reports
class Report(db.Model):
    __tablename__ = "reports"
    id = db.Column(db.Integer, primary_key=True)
    generated_at = db.Column(db.DateTime, server_default=db.func.now())
    report_data = db.Column(db.JSON)  # Store various analytics data