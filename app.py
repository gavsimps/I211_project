from flask import Flask, render_template, url_for, request, redirect
from os.path import exists
import csv
import html
import datetime

app = Flask(__name__)

app.config.from_pyfile(app.root_path + '/config_defaults.py')
if exists(app.root_path + '/config.py'):
    app.config.from_pyfile(app.root_path + '/config.py')

import database

MEMBER_PATH = app.root_path + '/members.csv'
MEMBER_KEYS = ['name','dob','email','address','phone']

TRIP_PATH = app.root_path + '/trips.csv'
TRIP_KEYS = ['name','start_date','length','cost','location','level','leader','description']

# MEMBER PATH
with open(MEMBER_PATH,'r') as csvfile:
    data = csv.DictReader(csvfile)
    membing = list(data)
    member_info = sorted(membing, key = lambda x:x['dob'])


# TRIP PATH
with open(TRIP_PATH,'r') as csvfile:
    data = csv.DictReader(csvfile)
    tripping = list(data)
    trips_info = sorted(tripping, key = lambda x:x['start_date'])

#MEMBERS FUNCTIONS
def get_members():
    with open(MEMBER_PATH, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        members = []
        for mem in data:
            members.append(mem)              
    return members

def set_members(gmem):
    with open(MEMBER_PATH, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=MEMBER_KEYS)
        writer.writeheader()
        for mems in gmem:
            writer.writerow(mems)


# TRIPS FUNCTIONS
def get_trips():
    with open(TRIP_PATH, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        trips_info = []
        for nature in data:
            trips_info.append(nature)
        trips = sorted(trips_info, key = lambda x:x['start_date'])              
    return trips

def set_trips(gtrip):
    with open(TRIP_PATH, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=TRIP_KEYS)
        writer.writeheader()
        for places in gtrip:
            writer.writerow(places)


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
        
        database.add_member(name,dob,email,address,phone)

        return redirect(url_for('members'))

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
        
        database.add_trip(name,start_date,length,cost,location,level,leader,description)

        return redirect(url_for('trips'))
    
    else:
        # TO DO: GET THIS TO SPECIFY WHERE ITS FROM
        return render_template('add_trip.html')

@app.route('/trips/<trip_id>')
def trip(trip_id=None):
    if trip_id :
        trip_info = database.get_trip(trip_id)
        return render_template('trip.html',trip_info=trip_info,trip=database.get_trip(trip_id))
    else:
        trips_info = database.get_trips()
        return render_template('trips.html',trips_info=trips_info)

# EDIT TRIPS
@app.route('/trips/<trip_id>/edit', methods=['GET','POST'])
def edit_trip(trip_id=None):
    trip_id = int(trip_id)
    trips = get_trips()

    if request.method == 'POST':
        tripedit = {}

        tripedit['name'] = request.form['name']
        tripedit['start_date'] = request.form['start']
        tripedit['length'] = request.form['length']
        tripedit['cost'] = request.form['cost']
        tripedit['location'] = request.form['locat']
        tripedit['level'] = request.form['level']
        tripedit['leader'] = request.form['leader']
        tripedit['description'] = request.form['desc']
        
        trips[trip_id] = tripedit
        set_trips(trips)

        return redirect(url_for('trips'))
    
    else: 
        trips = get_trips()
        return render_template('add_trip.html',trip=trips[trip_id],trip_id=trip_id)

@app.route('/trips/<trip_id>/delete', methods=['GET','POST'])
def del_trip(trip_id=None):
    trip_id = int(trip_id)
    trips=get_trips()
    if request.method == 'POST':
        trip=trips[int(trip_id)]
        trips.remove(trip)
        set_trips(trips)
        print(trips)
        
        return redirect(url_for('trips'))
    else:
        return render_template('del_trip.html',trip_id=trip_id,trips=trips,trip=trips[trip_id])
