from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class DeleteUserForm(FlaskForm):
    """Form for deleting a user."""
    
    username = StringField("Username")
    
    password = PasswordField("Password")