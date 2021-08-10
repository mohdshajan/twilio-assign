from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SECRET_KEY']='thisisfirstflaskapp'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/flask.db'

db=SQLAlchemy(app)
from python_twilio import routes