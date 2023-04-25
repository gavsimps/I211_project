from flask import Flask, render_template, url_for, request, redirect
from os.path import exists
import csv
import html
import datetime
import re 

app = Flask(__name__)

# CONFIG
app.config.from_pyfile(app.root_path + '/config_defaults.py')
if exists(app.root_path + '/config.py'):
    app.config.from_pyfile(app.root_path + '/config.py')

import database

# DATA VALIDATION

# COST FOR ADD/EDIT TRIP
def check_int(cost):
    error=''
    msg=[]
    if len(cost)>4:
        msg.append("Price is too expensive! Trips must not be more than $9999")
    if cost.isdigit() == False:
        msg.append('Invalid input for cost: Use only integers.')
    if len(msg)>0:
        error = " \n".join(msg)
    return error 

# PHONE FOR ADD/EDIT USER
def validate_phone_number(client_subitted_phone_number):
    phone_regex = '^\d{3}-\d{3}-\d{4}$'
    match = re.search(phone_regex, client_subitted_phone_number)
    return match 


# APPLICATION
@app.route('/')
def index():
    return render_template('index.html')

# MEMBERS
@app.route('/members')
def members():
    # member_info = sorted(get_members(), key = lambda x:x['DoB'])
    member_info = database.get_members()
    return render_template('members.html',member_info=member_info)

@app.route('/members/add', methods=['GET','POST'])
def add_member():
    if request.method == 'POST':

        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        address = request.form['addy']
        phone = request.form['phone']

        if validate_phone_number(phone):
            database.add_member(name,dob,email,address,phone)
            return redirect(url_for('members'))
        else:
            error = 'Unsupported phone type! Supported format: xxx-xxx-xxxx'
            return render_template('add_member.html', error=error)

    else:    
        return render_template('add_member.html')


# TRIPS
@app.route('/trips')
def trips():
    # trips_info = sorted(get_trips(), key = lambda x:x['start_date'])
    trips_info = database.get_trips()
    return render_template('trips.html',trips_info=trips_info)

@app.route('/trips/add', methods=['GET','POST'])
def add_trip():
    if request.method == 'POST':

        name = request.form['name']
        start_date = request.form['start']
        length = request.form['length']
        cost = request.form['cost']
        location = request.form['locat']
        level = request.form['level']
        leader = request.form['leader']
        description = request.form['desc']
        
        error = check_int(cost)
        if error:
            return render_template('add_trip.html', error=error,cost=cost)

        database.add_trip(name,start_date,length,cost,location,level,leader,description)

        return redirect(url_for('trips'))
    
    else:
        # TO DO: GET THIS TO SPECIFY WHERE ITS FROM
        return render_template('add_trip.html')

@app.route('/trips/<trip_id>')
def trip(trip_id=None):
    if trip_id :
        trip_info = database.get_trip(trip_id)
        attendees = database.get_attendees(trip_id)
        attend = database.get_member_attendee()
        return render_template('trip.html',trip_info=trip_info,trip=database.get_trip(trip_id),attendees=attendees,attend=attend)
    else:
        trips_info = database.get_trips()
        return render_template('trips.html',trips_info=trips_info)

# EDIT TRIPS
@app.route('/trips/<trip_id>/edit', methods=['GET','POST'])
def edit_trip(trip_id=None):
    if request.method == 'POST':

        name = request.form['name']
        start_date = request.form['start']
        length = request.form['length']
        cost = request.form['cost']
        location = request.form['locat']
        level = request.form['level']
        leader = request.form['leader']
        description = request.form['desc']

        error = check_int(cost)
        if error:
            return render_template('add_trip.html',trip=database.get_trip(trip_id),trips=trips,trip_id=trip_id,error=error,cost=cost)
        else:
            database.update_trip(name,start_date,length,cost,location,level,leader,description,trip_id)

        return redirect(url_for('trips'))
    
    else: 
        trips = database.get_trip(trip_id)
        return render_template('add_trip.html',trip=database.get_trip(trip_id),trips=trips,trip_id=trip_id)

@app.route('/trips/<trip_id>/delete', methods=['GET','POST'])
def del_trip(trip_id=None):
    
    if request.method == 'POST':
        
        database.delete_trip(trip_id)
        
        return redirect(url_for('trips'))
    else:
        trips = database.get_trip(trip_id)
        return render_template('del_trip.html',trip=database.get_trip(trip_id),trips=trips,trip_id=trip_id)

# NEW ATTENDEES TABLE IMPLEMENTATION
@app.route('/trips/<trip_id>/attendees/add')
def add_attendee():
    return redirect(url_for('trips/<trip_id>'))