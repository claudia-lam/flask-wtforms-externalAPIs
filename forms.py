"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Length, URL


class PetForm(FlaskForm):
    """Form for adding/editing a pet."""

    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=25)])

    species = StringField(
        "Species",
        validators=[Length(max=30), InputRequired()])

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
