from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class ReviewForm(FlaskForm):
    review_body = TextAreaField('Review', validators=[
        DataRequired(),
        Length(max=500, message="Review must be under 500 characters.")
    ])
    rating = IntegerField('Rating', validators=[
        DataRequired(),
        NumberRange(min=1, max=5, message="Rating must be between 1 and 5.")
    ])
    submit = SubmitField('Submit')
