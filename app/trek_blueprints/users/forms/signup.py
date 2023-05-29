"""Creates a signup form for the user."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, Optional
from email_validator import validate_email, EmailNotValidError

class AddUserForm(FlaskForm):
    """Form for adding users."""

    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])
    
    password = PasswordField("Password", validators=[InputRequired()])
    
    first_name = StringField("First Name", validators=[InputRequired(), Length(max=30)])
    
    last_name = StringField("Last Name", validators=[InputRequired(), Length(max=30)])
    
    avatar = StringField("Avatar", validators=[Optional()])
    
    bio = TextAreaField("Bio", validators=[Optional()])
    
    location = StringField("Location", validators=[Optional()])
    
