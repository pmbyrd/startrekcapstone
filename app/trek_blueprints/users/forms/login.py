from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

# Create login form with either username or email and password
class LoginForm(FlaskForm):
    """Form for logging in users."""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) #TODO - Add password strength validator
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')