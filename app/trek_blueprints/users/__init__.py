"""
This is the users blueprint module 

"""
from flask import Blueprint

users = Blueprint(
    "users",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/users",
)

from app.trek_blueprints.users import routes