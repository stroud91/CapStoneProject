from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Business


def business_name_exists(form, field):
    business_name = field.data
    business = Business.query.filter(Business.name == business_name).first()
    if business:
        raise ValidationError("Business with this name already exists.")

def valid_zip_code(form, field):
    if not field.data.isdigit() or len(field.data) != 5:
        raise ValidationError("Invalid ZIP Code.")

def valid_phone_number(form, field):
    if not field.data.isdigit() or len(field.data) != 10:
        raise ValidationError("Invalid phone number.")


class BusinessForm(FlaskForm):
    name = StringField('Business Name', validators=[
        DataRequired(),
        Length(min=1, max=50),
        business_name_exists
    ])

    description = StringField('Description', validators=[
        Length(max=255)
    ])

    address = StringField('Address', validators=[
        DataRequired(),
        Length(min=1, max=255)
    ])

    city = StringField('City', validators=[
        DataRequired(),
        Length(min=1, max=50)
    ])

    state = StringField('State', validators=[
        DataRequired(),
        Length(min=1, max=25)
    ])

    zip_code = StringField('ZIP Code', validators=[
        DataRequired(),
        Length(min=1, max=10),
        valid_zip_code
    ])

    phone_number = StringField('Phone Number', validators=[
        DataRequired(),
        Length(min=1, max=30),
        valid_phone_number
    ])

    about = StringField('About', validators=[
        DataRequired(),
        Length(min=1, max=500)
    ])

    type = StringField('Type', validators=[
        DataRequired(),
        Length(min=1, max=255)
    ])

    email = StringField('Email', validators=[

        Length(min=1, max=255)
    ])

    logo_id = FileField('Logo', validators=[
        DataRequired()
    ])

    owner_id = IntegerField('Owner ID', validators=[
        DataRequired()
    ])
