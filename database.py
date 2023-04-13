import pymysql
from app import app

def get_connection():
    return pymysql.connect(host=app.config['DB_HOST'],
                           user=app.config['DB_USER'],
                           password=app.config['DB_PASS'],
                           database=app.config['DB_DATABASE'],
                           cursorclass=pymysql.cursors.DictCursor)

def get_trips():
    '''Returns a list of dictionaries representing all of the trips data'''
    pass

def get_trip(trip_id):
    '''Takes a trip_id, returns a single dictionary containing the data for the trip with that id'''
    pass

def add_trip(trip):
    '''Takes as input all of the data for a trip. Inserts a new trip into the trip table'''
    pass

def update_trip(trip_id, trip):
    '''Takes a trip_id and data for a trip. Updates the trip table with new data for the trip with trip_id as it's primary key'''
    pass

def add_member(member):
    '''Takes as input all of the data for a member and adds a new member to the member table'''
    pass
    
def get_members():
    sql = "select * from member order by dob"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    pass

def edit_member(member_id, member):
    '''Given an member__id and member info, updates the data for the member with the given member_id in the member table'''
    pass

def delete_member(member_id):
    '''Takes a member_id and deletes the member with that member_id from the member table'''
    pass
    
def add_member_trip(trip_id, member_id):
    '''Takes as input a trip_id and a member_id and inserts the appropriate data into the database
    that indicates the member with member_id as a primary key is attending the trip with the trip_id as a primary key'''
    pass
    
def remove_member_trip(trip_id, member_id):
    '''Takes as input a trip_id and a member_id and deletes the data in the database that indicates that the member with member_id as a primary key 
    is attending the trip with trip_id as a primary key.'''
    pass
    
def get_attendees(trip_id):
    '''Takes a trip_id and returns a list of dictionaries representing all of the members attending the trip with trip_id as its primary key'''
    pass
