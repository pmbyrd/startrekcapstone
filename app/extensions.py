"""

./app/extensions.py

This file contains the flask extensions used by the application.

Placed here in the app folder for ease of use and so other files can easily import them.

"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
#STUB - 2021-07-20 - 11:00 - https://flask-login.readthedocs.io/en/latest/#configuring-loginmanager