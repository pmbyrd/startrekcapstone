from flask import render_template
from app.trek_blueprints.users import users

@users.route('/')
def index():
    return render_template('users/index.html')

@users.route('/new_user')
def new_user():
    """Renders a form to create a new user"""

    return render_template('users/new_user.html')