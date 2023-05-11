from flask import Flask
from .controller import *


def create_app():
    app = Flask(__name__)

    with app.app_context():
        app.register_blueprint(user_api)
        app.register_blueprint(point_api)

    return app
