"""
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

# Add product form - used to add new products to the database
class AddProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    on_hand_count = IntegerField('Current Count', validators=[DataRequired(), NumberRange(min=0, message="You cannot enter a negative count")])
    submit = SubmitField('Add Product')

# Remove product form - used to remove produces from the database
class RemoveProductForm(FlaskForm):
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    submit = SubmitField('Remove Product')

# Place an order for a certain amount of a product
class OrderProductForm(FlaskForm):
    product_id = IntegerField('Product ID')
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1, message="You must enter a positive value")])
    submit = SubmitField('Place Order')

# Create an alert for a particular product
class AlertForm(FlaskForm):
    product_id = IntegerField('Product ID')
"""
