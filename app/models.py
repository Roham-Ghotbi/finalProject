import sqlite3 as sql

# user functions

def insert_user(username, password):
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
    	con.commit()
    	return cur.lastrowid

def retrieve_user(username):
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	return str(cur.execute('select user_id from users where username = "' + username + '"').fetchone()[0]) # why is it in tuple form??

def retrieve_password(username):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return str(cur.execute('SELECT password from users where username = "' + username +'"').fetchone()[0])
# trip functions

def insert_trip(trip_name, destination, owner_id, friend_id):
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	cur.execute("INSERT INTO trips (trip_name, destination, owner_id, friend_id) VALUES (?,?,?,?)", (trip_name, destination, owner_id, friend_id))
    	con.commit()
        return cur.lastrowid

def retrieve_trips(username):
    uid = retrieve_user(username)
    with sql.connect("database.db") as con:
    	con.row_factory = sql.Row
    	cur = con.cursor()
        result = cur.execute('select * from trips where owner_id = "' + uid + '" or friend_id = "' + uid + '"').fetchall() 
    	return result

def delete_trip(trip_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE from trips where trip_id = " + trip_id)
        con.commit()
        return cur.lastrowid

