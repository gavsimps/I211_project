from flask import Flask, render_template, url_for, request, redirect
import csv
import datetime

app = Flask(__name__)

MEMBER_PATH = app.root_path + '/members.csv'
MEMBER_KEYS = ['Name','DoB','Email','Address','Phone']

TRIP_PATH = app.root_path + '/trips.csv'
TRIP_KEYS = ['name','start_date','length','cost','location','level','leader','description']

# MEMBER PATH
with open(MEMBER_PATH,'r') as csvfile:
    lines = csv.reader(csvfile)
    member_header = []
    for row in lines:
        member_header.append(row)

with open(MEMBER_PATH,'r') as csvfile:
    data = csv.DictReader(csvfile)
    membing = list(data)
    member_info = sorted(membing, key = lambda x:x['DoB'])


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
        trips = []
        for nature in data:
            trips.append(nature)              
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
    member_info = get_members()
    return render_template('members.html',member_info=member_info,member_header=member_header)

@app.route('/members/add', methods=['GET','POST'])
def add_member():
    if request.method == 'POST':
        gmem = get_members()
        memberadd = {}

        memberadd['Name'] = request.form['name']
        memberadd['DoB'] = request.form['dob']
        memberadd['Email'] = request.form['email']
        memberadd['Address'] = request.form['addy']
        memberadd['Phone'] = request.form['phone']
        
        gmem.append(memberadd)
        set_members(gmem)

        return redirect(url_for('members'))

    else:    
        return render_template('add_member.html')







# TRIPS
@app.route('/trips')
def trips():
    trips_info = get_trips()
    return render_template('trips.html',trips_info=trips_info)

@app.route('/trips/add', methods=['GET','POST'])
def add_trip():
    if request.method == 'POST':
        gtrip = get_trips()
        tripadd = {}

        tripadd['name'] = request.form['name']
        tripadd['start_date'] = request.form['start']
        tripadd['length'] = request.form['length']
        tripadd['cost'] = request.form['cost']
        tripadd['location'] = request.form['locat']
        tripadd['level'] = request.form['level']
        tripadd['leader'] = request.form['leader']
        tripadd['description'] = request.form['desc']
        
        gtrip.append(tripadd)
        set_trips(gtrip)

        print(tripadd)
        return redirect(url_for('trips'))
    
    else:
        return render_template('add_trip.html')

@app.route('/trips/<trip_id>')
def trip(trip_id=None):
    if trip_id == trip_id:
        trip_page = trips_info[int(trip_id)]
        return render_template('trip.html',trip_page=trip_page)
    else:
        return render_template('trips.html',trips_info=trips_info)
    
@app.route('/trips/<trip_id>/edit')
def edit_trip():
    return render_template('trip_form.html')
