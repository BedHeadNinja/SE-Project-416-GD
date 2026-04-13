from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Base login form
class LoginForm(FlaskForm):
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# ID form
class IDForm(LoginForm):
    username = StringField('Employee ID', validators=[DataRequired()])

# Password form
class PasswordForm(LoginForm):
    password = PasswordField('Password', validators=[DataRequired()])
