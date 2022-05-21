from importlib import import_module
from dynaconf import FlaskDynaconf


def load_extensions(app):
    for extension in app.config.GET('EXTENSIONS'):
        mod = import_module(extension)
        mod.init_app(app)


def init_app(app):
    FlaskDynaconf.init_app(app)
