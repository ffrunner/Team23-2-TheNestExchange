from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis


def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    
    app.register_blueprint(auth)
    return app

