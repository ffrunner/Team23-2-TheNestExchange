from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from routes import auth


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql+psycopg2://{user}:{password}@{host}/{database}'
db = SQLAlchemy(app)

app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)

