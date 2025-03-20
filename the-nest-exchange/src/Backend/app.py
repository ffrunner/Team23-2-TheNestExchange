from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis



app = Flask(__name__)
db = SQLAlchemy(app)

app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)

