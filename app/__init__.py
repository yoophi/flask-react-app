from flask import Flask

from .extensions import CORS


def create_app():
    app = Flask(__name__, static_folder='../react-app/build')

    init_extensions(app)
    init_blueprint(app)

    return app


def init_blueprint(app):
    from .api import api as api_bp
    from .main import main as main_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(main_bp)


def init_extensions(app):
    CORS(app, resources={
        r"/api/*": {"origins": "*"},
        r"/oauth/*": {"origins": "*"},
        r"/swagger/*": {"origins": "*"},
    })
