"""This module contains the user model for the database."""

from app.extensions import db
from flask_bcrypt import Bcrypt 


bcrypt = Bcrypt()

DEFAULT_IMAGE_URL = "https://loading.io/icon/tpi8gu"


class User(db.Model):
    """Creates a user model for the database.
    
    Attributes:
        id: An integer representing the user's id.
        username: A string representing the user's username.
        first_name: A string representing the user's first name.
        last_name: A string representing the user's last name.
        email: A string representing the user's email.
        avatar: A string representing the user's avatar.
        password: A string representing the user's password.
        bio: A string representing the user's bio.
        location: A string representing the user's location.
        
    """
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.Text, nullable=False, unique=True)
    
    first_name= db.Column(db.Text, nullable=False)
    
    last_name = db.Column(db.Text, nullable=False)
    
    email = db.Column(db.Text, nullable=False, unique=True)
    
    avatar = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
    password = db.Column(db.Text, nullable=False)
    
    bio = db.Column(db.Text, nullable=True)
    
    location = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
    
#     # comments = db.relationship("Comment", backref="user", cascade="all, delete-orphan")
    
#     # posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")
    
#     # tags = db.relationship("Tag", backref="user", cascade="all, delete-orphan")
    
    
    
    @classmethod
    def signup(cls, username, email, password, first_name, last_name, avatar, bio):
        """Signs up a user: hashes their password and adds user to system."""
        
        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')
        
        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
            bio=bio
        )
        
        db.session.add(user)
        return user
    
    
    @classmethod
    def authenticate(cls, username, password, email):
        """Find user with `username` and `password`. If found, return user, else return False."""
        
        user = cls.query.filter_by(username=username).first()
        
        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                bcrypt.check_password_hash(user.password, password)
                if is_auth:
                    return user
                
        return False
    

#create a fake user
user = User()   