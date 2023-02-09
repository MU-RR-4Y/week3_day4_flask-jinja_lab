from flask import render_template, request,redirect
from app import app
from models.event_object import events, add_new_event
from models.events import Events
import datetime


@app.route('/')
def index():
    return render_template('index.html', title = 'Home', events = events)

@app.route('/new_event')
def new_event():
    return render_template('new_event.html', title = 'New Event')

@app.route('/', methods=['POST'])
def add_event():
    event_date = (request.form['date'])
    event_name = request.form['name']
    event_number_of_guests = request.form['number_of_guests']
    event_location = request.form['location']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Events(event_date,event_name,event_number_of_guests,event_location,event_description, event_recurring)
    add_new_event(new_event)
    return redirect('/')

