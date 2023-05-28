"""
../app/main/__init__.py

This file contains the main blueprint. 

Handles general routes throughout the application.

"""
from flask import Blueprint

main = Blueprint('main', __name__)

#NOTE - Added to avoid circular imports
from app.main import routes