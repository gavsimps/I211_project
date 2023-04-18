import pymysql
from app import app

def get_connection():
    return pymysql.connect(host=app.config['DB_HOST'],
                           user=app.config['DB_USER'],
                           password=app.config['DB_PASS'],
                           database=app.config['DB_DATABASE'],
                           cursorclass=pymysql.cursors.DictCursor)

def get_trips():
    # '''Returns a list of dictionaries representing all of the trips data'''
    sql = "select * from trips order by start_date"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

def get_trip(trip_id):
    # '''Takes a trip_id, returns a single dictionary containing the data for the trip with that id'''
    sql = "select * from trips where id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchall()

def add_trip(name,start_date,length,cost,location,level,leader,description):
    # '''Takes as input all of the data for a trip. Inserts a new trip into the trip table'''
    sql = "insert into trips (name,start_date,length,cost,location,level,leader,description) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name,start_date,length,cost,location,level,leader,description))
            return cursor.fetchall()
    pass

def update_trip(name,start_date,length,cost,location,level,leader,description,trip_id):
    # '''Takes a trip_id and data for a trip. Updates the trip table with new data for the trip with trip_id as it's primary key'''
    sql = "update trips set name=%s,start_date=%s,length=%s,cost=%s,location=%s,level=%s,leader=%s,description=%s where id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name,start_date,length,cost,location,level,leader,description,trip_id))
            return cursor.fetchall()
    pass

def delete_trip(trip_id):
    # '''Takes a trip_id and data for a trip. Updates the trip table with new data for the trip with trip_id as it's primary key'''
    sql = "delete from trips where id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchall()
    pass

def add_member(name,dob,email,address,phone):
    # '''Takes as input all of the data for a member and adds a new member to the member table'''
    sql = "insert into members (name,dob,email,address,phone) values (%s,%s,%s,%s,%s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name,dob,email,address,phone))
            return cursor.fetchall()
    
def get_members():
    sql = "select * from members order by dob"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

def edit_member(member_id,name,dob,email,address,phone):
    # '''Given an member_id and member info, updates the data for the member with the given member_id in the member table'''
    sql = "update members name=%s,dob=%s,email=%s,address=%s,phone=%s where id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name,dob,email,address,phone,member_id))
            return cursor.fetchall()
    pass

def delete_member(member_id):
    # '''Takes a member_id and deletes the member with that member_id from the member table'''
    sql = "delete from members where id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (member_id))
            return cursor.fetchall()
    pass
    
def add_member_trip(trip_id, member_id):
    # '''Takes as input a trip_id and a member_id and inserts the appropriate data into the database
    # that indicates the member with member_id as a primary key is attending the trip with the trip_id as a primary key'''
    sql = "insert into attend (member_id,trip_id) values (%s,%s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (member_id,trip_id))
            return cursor.fetchall()
    pass
    
def remove_member_trip(trip_id, member_id):
    # '''Takes as input a trip_id and a member_id and deletes the data in the database that indicates that the member with member_id as a primary key 
    # is attending the trip with trip_id as a primary key.'''
    sql = "delete from attend where member_id = %s and trip_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (member_id,trip_id))
            return cursor.fetchall()
    pass
    
def get_attendees(trip_id):
    # '''Takes a trip_id and returns a list of dictionaries representing all of the members attending the trip with trip_id as its primary key'''
    sql = "select t.id, m.name from trips as t join attend as a on a.trip_id = t.id join members as m on m.id = a.member_id where t.id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchall()
    pass
