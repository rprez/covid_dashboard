from flask import Flask
from .errors import page_not_found, internal_server_error
from .MongoEncoder import MongoJsonEncoder
from os import environ

def create_app():

    app = Flask(__name__)
    app.json_encoder = MongoJsonEncoder

    if environ['ENV'] == "production":
        app.config.from_object("application.config.ProductionConfig")
    elif environ['ENV'] == "testing":
        app.config.from_object("application.config.TestingConfig")
    elif environ['ENV'] == "develop_and_testing":
        app.config.from_object("application.config.DevelopmentAndTestingDebug")
    else:
        app.config.from_object("application.config.DevelopmentConfig")

    print(f'ENV is set to: {app.config["ENV"]}')

    with app.app_context():
        # Include our Routes
        from application.routes import admin

        # Register Blueprints
        app.register_blueprint(admin)

        # Register Errors Handler
        app.register_error_handler(404, page_not_found)
        app.register_error_handler(500, internal_server_error)

    return app
