from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, FileField, validators

class DishForm(FlaskForm):
    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=2, max=100)
    ])
    description = TextAreaField('Description', [
        validators.Optional(),
        validators.Length(max=500)
    ])
    price = FloatField('Price', [
        validators.DataRequired(),
        validators.NumberRange(min=0)
    ])
    image = FileField('Image', [
        validators.Optional()
    ])
    category_id = IntegerField('Category ID', [
        validators.DataRequired()
    ])
