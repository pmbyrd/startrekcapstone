from flask import render_template, redirect, flash
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.trek_blueprints.users import users
from app.trek_blueprints.users.models.user import User, DEFAULT_IMAGE_URL
from app.trek_blueprints.users.forms.signup import AddUserForm
from app.main.routes import test

@users.route('/')
def index():
    return render_template('users/index.html')

@users.route('/signup')
def new_user():
    """Renders a form to create a new user"""
    
    signup_form = AddUserForm()
    return render_template('users/signup.html', form=signup_form)

@users.route('/signup', methods=['POST'])
def create_user():
    """Creates a new user"""
    
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
            print ("""*************************************
            {new_user.username} created successfully
            *************************************""")
            flash("User created successfully", 'success')
            return redirect('users/secret')
        except IntegrityError:
            flash("Username or email already taken", 'danger')
            return redirect('/signup')
        
            #TODO - 1. implement login functionality
            #TODO - 2. redirect to the user's profile page
            #NOTE - return redirect(f'/users/{new_user.id}')
    return redirect('/signup')
        
@users.route('users/secret')
def secret():
    return render_template('users/secret.html')

@users.route('/<int:user_id>')
def show_user(user_id):
    """Shows a user's profile page"""
    
    #TODO - show a user's profile page
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@users.route('/<int:user_id>/edit')
def edit_user(user_id):
    """Renders a form to edit a user's profile"""
    
    #TODO - render a form to edit a user's profile
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)