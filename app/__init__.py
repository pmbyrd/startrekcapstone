"""
.__init__.py is a special file that tells Python that this directory should be treated as a package.

This file while handle the blueprint registration, the creation of the Flask application object and the instantiation of the extensions.

"""

from flask import Flask
from config import Config
from .extensions import db, migrate
#TODO - Be sure to import each blueprint here before registering them

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = 'you-will-never-guess'
    # Initialize Flask extensions here
    db.init_app(app)
    # db.create_all()
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()

    # Register blueprints here
    from app.main import main as main_bp
    app.register_blueprint(main_bp)
    from app.trek_blueprints.posts import posts as posts_bp
    app.register_blueprint(posts_bp)
    from app.trek_blueprints.users import users as users_bp
    app.register_blueprint(users_bp)
    
    return app
