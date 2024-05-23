""" set app with flask"""
import os
from flask import Flask
from flasgger import Swagger
from .models import db
from .taxis import taxis_routes
from .trajectories import trajectories
from .last_trajectory import last_trajectory


def create_app():
    """Create app"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URL_CONECTION')

    # set bd up with flask
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(taxis_routes)
    app.register_blueprint(trajectories)
    app.register_blueprint(last_trajectory)

   # Initialize Swagger
    Swagger(app)

    return app


if __name__ == "__app__":
    app = create_app()
    app.run(debug=True)
