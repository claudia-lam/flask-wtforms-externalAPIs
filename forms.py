"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Length, URL


class PetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=25)])

    species = SelectField(
        "Species",
        validators=[InputRequired()], choices=[
            ('dog', 'Dog'),
            ('cat', 'Cat'),
            ('porcupine', 'Porcupine')
        ])

    photo_url = StringField(
        "Photo URL",
        validators=[URL()])

    age = SelectField('Age',
                      validators=[InputRequired()],
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')])

    notes = TextAreaField(
        "Notes",
        validators=[Optional()]
    )

    available = BooleanField(
        'Available')


class PetEditForm(FlaskForm):
    """Form to edit a pet. """

    photo_url = StringField(
        "Photo URL",
        validators=[URL()])

    notes = TextAreaField(
        "Notes",
        validators=[Optional()]
    )

    available = BooleanField(
        'Available')
