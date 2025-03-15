from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .auth import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nestexchange'
db = SQLAlchemy(app)

app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
