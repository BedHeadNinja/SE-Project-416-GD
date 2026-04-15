from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

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

# Form for adding new products
# !!INCOMPLETE!!
class AddProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    on_hand_count = IntegerField('Current Count', validators=[DataRequired(), NumberRange(min=0, message="You cannot enter a negative count")])
    submit = SubmitField('Add Product')
