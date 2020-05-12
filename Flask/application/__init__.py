from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('FLASK_TEST_DB_URI')
app.config['SECRET_KEY'] = getenv('FLASK_SECRET_KEY')

db = SQLAlchemy(app)

from application import routes