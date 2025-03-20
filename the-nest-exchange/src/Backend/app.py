from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis


def create app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    
    app.register_blueprint(auth)
    return app


if __name__ == '__main__':
    app.run(debug=True)

