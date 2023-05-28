from flask import render_template
from app.trek_blueprints.users import users

@users.route('/')
def index():
    return render_template('users/index.html')