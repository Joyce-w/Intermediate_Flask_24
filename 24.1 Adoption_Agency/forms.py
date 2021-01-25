from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField, BooleanField, SelectField
from wtforms.validators import InputRequired, NumberRange, URL, Optional


available_species = ['dog', 'cat', 'deer', 'chinchilla', 'frog', 'chicken', 'porcupine']

class AddPetForm(FlaskForm):
    """Form for adding new pets"""
    name = StringField("Name", validators=[InputRequired(message="Please add a name for the pet")])
    
    species = SelectField('Programming Language', choices=[(sp,sp) for sp in available_species])

    photo_url = StringField("Photo Url",validators=[URL(message="Please enter valid url image"), Optional()])

    age = FloatField("Age",validators=[NumberRange(min=0, max=30), Optional()])

    notes = StringField("Additional Notes", validators=[Optional()])

    available = BooleanField("Available", validators=[Optional()])