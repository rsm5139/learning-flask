from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SocialApp(db.Model):
    __tablename__ = 'step_4'
    uid     = db.Column(db.Integer, primary_key = True)
    name    = db.Column(db.String(100))
    comment = db.Column(db.String(140))
    
    def __init__(self, name, comment):
        self.name    = name.title()
        self.comment = comment