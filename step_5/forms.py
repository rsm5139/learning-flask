from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CommentForm(Form):
    name    = StringField('name', validators=[DataRequired()])
    comment = StringField('comment', validators=[DataRequired()])
    submit  = SubmitField('Post')