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

# Update the on hand count for a product
class UpdateQuantityForm(FlaskForm):
    product_id = IntegerField('Product ID')
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1, message="You must enter a positive value")])
    submit = SubmitField('Update Quantity')

# Set the low stock warning
class SetThresholdForm(FlaskForm):
    product_id = IntegerField('Product ID')
    stock_alert_minimum = IntegerField('Warning Minimum', validators=[DataRequired(), NumberRange(min=1, message="You must enter a positive value")])
    submit = SubmitField('Set Threshold')
