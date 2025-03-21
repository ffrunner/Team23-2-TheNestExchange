from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Team23_2@database-1.cjm0e6m6u6vm.us-east-2.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "This is the landing page"

if __name__== "__main__":
    app.run(debug=True)


