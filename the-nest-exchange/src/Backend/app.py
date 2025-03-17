from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:Team23_2@database-1.cjm0e6m6u6vm.us-east-2.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)

app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)
