from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'step_5'
    uid        = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(25))
    last_name  = db.Column(db.String(25))
    email      = db.Column(db.String(120), unique = True)
    pwdhash    = db.Column(db.String(100))
    
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name.title()
        self.last_name  = last_name.title()
        self.email      = email.lower()
        self.set_password(password)
    
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)