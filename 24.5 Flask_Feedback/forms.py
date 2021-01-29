from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField

class AddRegistrationForm(FlaskForm):
    """Form for user signup"""
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("Username")
    password = PasswordField("Password")
    email = StringField("Email")

class LoginForm(FlaskForm):
    """Form for login"""
    username = StringField("Username")
    password = PasswordField("Password")
