import os

from flask import Flask
from instance.config import app_config
from app.api.v1 import views


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    #register blueprints
    app.register_blueprint(views.admin)
    app.register_blueprint(views.attendant)


    return app