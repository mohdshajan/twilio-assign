import os
import flask
from twilio.rest import Client

from flask.helpers import url_for
from twilio.rest.api.v2010.account import message
from werkzeug.utils import redirect
from python_twilio import app, db
from flask import render_template,url_for,redirect,flash
from flask import Flask, request
from python_twilio.forms import RegistrationForm, LoginForm
from python_twilio.models import Message_Details, User

from datetime import date, datetime

import logging
logging.basicConfig(level=logging.INFO)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


# @app.route('/')
# def root():
#    return "Ahoy Twilio"

@app.route('/home')
def homepage():
    return render_template('home.html', title='HomePage')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html', title='Account')

@app.route('/register', methods=["POST","GET"])
def register():
    form=RegistrationForm()
    sender = '+18317773819'

    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,mobilenumber=form.mobilenumber.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Message sent successfully to {form.mobilenumber.data}',category='success') 
        recipient = form.mobilenumber.data
        message = client.messages.create(
            body='Hi You have successfully signed-up! Welcome to Melbourne Dental Clinic. For appointments,please use online booking ',
            from_=sender,
            status_callback='http://eca74ad7a3bb.ngrok.io',
            to=recipient
            )
        print(message.sid)
        #message_details = client.messages(message.sid).fetch()
        #return render_template('home.html')

    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    sender = '+18317773819'
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if form.email.data==user.email and form.password.data==user.password:
            flash(f'Login Successful for {form.email.data}',category='success')
            return redirect(url_for('homepage'))
        else:
            flash(f'Login Unsuccessful for {form.email.data}',category='danger')
            return redirect(url_for('register'))
    
    return render_template('login.html', title='Login', form=form)

from datetime import date, datetime

@app.route('/', methods=['POST'])

@app.route('/messages_status', methods=['POST'])
def messages_status():
    message_sid = request.values.get('MessageSid', None)
    message_status = request.values.get('MessageStatus', None)
    to = request.values.get('To', None)

    date_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    msg=Message_Details(ssd_id=message_sid, status=message_status, mobile_number=to, date_time=date_time)
    db.session.add(msg)
    db.session.commit()
    return None


@app.route('/messages_details', methods=['GET'])
def messages_details():

    msgs = Message_Details.query.all()

    return render_template('messages.html', msgs=msgs)