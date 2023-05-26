from flask import Blueprint

posts = Blueprint(
    "posts",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/posts",
)


from app.trek_blueprints.posts import routes
