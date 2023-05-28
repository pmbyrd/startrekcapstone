""" This is a module for seeding the database with users.
    Currently, it drops all tables and recreates them.
    Populated with a csv file of users.
"""

import os
from csv import DictReader
from app.extensions import db
from app.trek_blueprints.users.models.user import User, DEFAULT_IMAGE_URL

def seed_users():
    # Define a list of random first and last names to choose from
    db.drop_all()
    db.create_all()

    # Get the path to the users.csv file based on the location of this file
    users_csv = os.path.join(os.path.dirname(__file__), '..', 'generator', 'users.csv')
    with open(users_csv) as users:
        user_dicts = list(DictReader(users))
        for user_dict in user_dicts:
            email = user_dict['email']
            username = user_dict['username']
            if User.query.filter_by(email=email).first() is not None:
                print(f"Skipping user {username} with email {email}: email already exists")
            elif User.query.filter_by(username=username).first() is not None:
                print(f"Skipping user {username} with email {email}: username already exists")
            else:
                user = User(**user_dict)
                db.session.add(user)
                print(f"Added user {username} with email {email}")
        
        db.session.commit()

def seed_db():
    seed_users()

seed_db()