from flask import render_template, redirect, flash
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.trek_blueprints.users import users
from app.trek_blueprints.users.forms.signup import AddUserForm
from app.main.routes import test

@users.route('/')
def index():
    return render_template('users/index.html')

@users.route('/signup')
def new_user():
    """Renders a form to create a new user"""
    
    #TODO - create a form to create a new user
    signup_form = AddUserForm()

    return render_template('users/signup.html', form=signup_form)

@users.route('/signup', methods=['POST'])
def create_user():
    """Creates a new user"""
    
    #TODO - create a new user
    form = AddUserForm()
    if form.validate_on_submit():
        try:
            new_user = User.signup(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                avatar=form.avatar.data,
                bio=form.bio.data,
                location=form.location.data
            )

            db.session.add(new_user)
            db.session.commit()
            flash("User created successfully", 'success')
        except IntegrityError:
            flash("Username or email already taken", 'danger')
            return redirect('/users/signup')
        
            #TODO - 1. implementent login functionality
            #TODO - 2. redirect to the user's profile page
            #NOTE - return redirect(f'/users/{new_user.id}')
    return redirect('/users/signup')

