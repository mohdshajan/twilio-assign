from python_twilio import db
from datetime import datetime


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    mobilenumber=db.Column(db.String(30),unique=False,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(20),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    # for displaying results when we call the user model- self refers to the class User
    def __repr__(self):
        return f'{self.username} : {self.email} : {self.date_created}'


class Message_Details(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ssd_id=db.Column(db.String(20),unique=True,nullable=False)
    status=db.Column(db.String(120),unique=True,nullable=False)
    mobile_number=db.Column(db.String(30),unique=False,nullable=False)
    date_time =db.Column(db.String(120),unique=False,nullable=False)