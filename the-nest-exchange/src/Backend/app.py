from flask import Flask
from auth import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Team23_2@database-1.cjm0e6m6u6vm.us-east-2.rds.amazonaws.com/postgres'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "This is the landing page"
app.register_blueprint(auth_bp)
if__name__== "__main__":
    app.run(debug=True)


