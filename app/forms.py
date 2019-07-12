from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Balhead Name', validators=[DataRequired(message='Username required!')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Balhead recollection?')
    submit = SubmitField('Sign In')