"""
.__init__.py is a special file that tells Python that this directory should be treated as a package.

This file while handle the blueprint registration, the creation of the Flask application object and the instantiation of the extensions.

"""

from flask import Flask
from config import Config
from .extensions import db, migrate, login_manager
#TODO - Be sure to import each blueprint here before registering them

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = 'you-will-never-guess'
    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    app.app_context().push() #?May not be needed
    #!SECTION - Flask-Login
    # login_manager.init_app(app)
    # login_manager.login_view = 'users.login'
    # login_manager.init_app(app)
    # Register blueprints here
    from app.main import main as main_bp
    app.register_blueprint(main_bp)
    from app.trek_blueprints.posts import posts as posts_bp
    app.register_blueprint(posts_bp)
    from app.trek_blueprints.users import users as users_bp
    app.register_blueprint(users_bp)

    #NOTE Login manager imports
    from app.trek_blueprints.users.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    return app
