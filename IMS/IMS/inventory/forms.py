from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange

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
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1, message="You must enter a positive value")])
    submit = SubmitField('Place Order')

class AddEmployeeForm(FlaskForm):
    submit = SubmitField('Add Employee')
    name = StringField('Name', validators=[DataRequired()])
    id = IntegerField('ID', validators=[DataRequired(), NumberRange(min=0, message="You cannot enter a negative count")])
    role = SelectField('Role', choices=[('Employee','Employee'), ('Manager', 'Manager')], validators=[DataRequired()])

# Update the on hand count for a product
class UpdateQuantityForm(FlaskForm):
    product_id = IntegerField('Product ID')
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1, message="You must enter a positive value")])
    submit = SubmitField('Update Quantity')
