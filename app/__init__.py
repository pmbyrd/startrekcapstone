"""
.__init__.py is a special file that tells Python that this directory should be treated as a package.

This file while handle the blueprint registration, the creation of the Flask application object and the instantiation of the extensions.

"""

from flask import Flask

from config import Config
from app.extensions import db, migrate, login_manager

#TODO - Be sure to import each blueprint here before registering them

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # *Initialize the Flask extensions here*
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # *Register the blueprints here*

    #FIXME - Testing routes
    @app.route('/')
    def index():
        return '<h1>Hello, World!</h1>'

    # *Initialize the app context here*
    with app.app_context():
        db.init_db()

    return app


