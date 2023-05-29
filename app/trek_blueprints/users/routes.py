from flask import render_template
from app.trek_blueprints.users import users
from app.trek_blueprints.users.forms.signup import AddUserForm

@users.route('/')
def index():
    return render_template('users/index.html')

@users.route('/signup')
def new_user():
    """Renders a form to create a new user"""
    
    #TODO - create a form to create a new user
    signup_form = AddUserForm()

    return render_template('users/signup.html', form=signup_form)

