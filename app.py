from flask import Flask, render_template, url_for, request, redirect
import csv
import datetime

app = Flask(__name__)

MEMBER_PATH = app.root_path + '/members.csv'
TRIP_PATH = app.root_path + '/trips.csv'

with open(MEMBER_PATH,'r') as csvfile:
    lines = csv.reader(csvfile)
    member_header = []
    for row in lines:
        member_header.append(row)

with open(MEMBER_PATH,'r') as csvfile:
    data = csv.DictReader(csvfile)
    membing = list(data)
    member_info = sorted(membing, key = lambda x:x['DoB'])


    
with open(TRIP_PATH,'r') as csvfile:
    data = csv.DictReader(csvfile)
    tripping = list(data)
    trips_info = sorted(tripping, key = lambda x:x['start_date'])



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def members():
    return render_template('members.html',member_info=member_info,member_header=member_header)

@app.route('/trips')
def trips():
    return render_template('trips.html',trips_info=trips_info)

@app.route('/trips/<trip_id>')
def trip(trip_id=None):
    if trip_id == trip_id:
        trip_page = trips_info[int(trip_id)]
        return render_template('trip.html',trip_page=trip_page)
    else:
        return render_template('trips.html',trips_info=trips_info)
