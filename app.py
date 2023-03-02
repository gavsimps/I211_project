from flask import Flask, render_template, url_for
import csv

app = Flask(__name__)

with open('members.csv','r') as csvfile:
    lines = csv.reader(csvfile)
    member_header = []
    for row in lines:
        member_header.append(row)

with open('members.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    members_info = {row['Name']:{'Name':row['Name'],'DoB':row['DoB'],'Email':row['Email'],
    'Address':row['Address'],'Phone':row['Phone']} for row in data}
    
with open('trips.csv','r') as csvfile:
    read = csv.reader(csvfile)
    trip_head = []
    for row in read:
        trip_head.append(row)
    trips_info= {}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def members():
    return render_template('members.html',members_info=members_info,member_header=member_header)

@app.route('/trips')
def trips():
    return render_template('trips.html')
