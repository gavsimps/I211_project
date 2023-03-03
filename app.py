from flask import Flask, render_template, url_for
import csv
import datetime

app = Flask(__name__)

with open('members.csv','r') as csvfile:
    lines = csv.reader(csvfile)
    member_header = []
    for row in lines:
        member_header.append(row)

with open('members.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    membing = list(data)
    member_info = sorted(membing, key = lambda x:x['DoB'])


    
with open('trips/trips.csv','r') as csvfile:
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
@app.route('/trips/<trip_id>')
def trips(trip_id=None):
    print(trip_id)
    if trip_id in trips_info:
        trip_info = trips_info[trip_id]
        return render_template('trip.html',trip_info=trip_info)
    else:
        return render_template('trips.html',trips_info=trips_info)
