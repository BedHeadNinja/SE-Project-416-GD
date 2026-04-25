from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange

class AddEmployeeForm(FlaskForm):
    submit = SubmitField('Add Employee')
    name = StringField('Name', validators=[DataRequired()])
    id = IntegerField('ID', validators=[DataRequired(), NumberRange(min=0, message="You cannot enter a negative count")])
    role = SelectField('Role', choices=[('Employee','Employee'), ('Manager', 'Manager')], validators=[DataRequired()])

class RemoveEmployeeForm(FlaskForm):
    submit = SubmitField('Remove Employee')
    id = IntegerField('ID', validators=[DataRequired(), NumberRange(min=0, message="You cannot enter a negative count")])
    