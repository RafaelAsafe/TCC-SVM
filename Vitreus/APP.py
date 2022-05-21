from flask import Flask
from vitreus.ext import configuration


def minimal_app():
    app = Flask(__name__)
    configurations.init_app(app)
    return app


def create_app():
    app = minimal_app()
    configurations.load_extensions(app)
    return app
