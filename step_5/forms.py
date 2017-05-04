from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class Login(Form):
    email    = StringField('email', validators=[DataRequired(), Email("Enter a valid email")])
    password = PasswordField('password', validators=[DataRequired()])
    submit   = SubmitField('Post')
    
class Register(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name  = StringField('last_name', validators=[DataRequired()])
    email      = StringField('email', validators=[DataRequired(), Email("Enter a valid email")])
    password   = PasswordField('password', validators=[DataRequired(), Length(min=6, max=25, message="Passwords must be 6-25 characters long.")])
    submit     = SubmitField('Post')