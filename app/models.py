import sqlite3 as sql
#Securing password Storage
import hashlib, uuid

##### USER #####
def hashPass(username, password):
    #hashMethod for securely storing password
    salt = hashlib.sha512(username).hexdigest()
    return hashlib.sha512(password + salt).hexdigest()

def insert_user(username, first_name, last_name, password):
    # returns user_id
    with sql.connect("database.db") as con:
        cur = con.cursor()
        # if retrieve_user_id(username) == None:   #to be fixed
        password = hashPass(username, password)
        cur.execute("INSERT INTO users (email, first_name, last_name, password) VALUES (?,?,?,?)", (username, first_name, last_name, password))
        con.commit()
        return cur.lastrowid
        # else:
        #     return -1

def retrieve_user(username):
    # returns user as a dictionary
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM users WHERE email = ?", (username,)).fetchone()
        return result

def retrieve_user_id(username):
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	return str(cur.execute("SELECT user_id FROM users WHERE email = ?", (username, )).fetchone()[0]) # why is it in tuple form??

def retrieve_all_emails():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return cur.execute('SELECT username FROM users').fetchall()

def retrieve_password(username):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return str(cur.execute("SELECT password FROM users WHERE email = ?", (username, )).fetchone()[0])

##### PROJECT #####

def insert_project(project_name, description, due_date, user_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO projects (project_name, description, due_date, user_id) VALUES (?,?,?,?)", (project_name, description, due_date, user_id))
        con.commit()
    # TODO: Add update functionality

def retrieve_project(project_id):
    # returns project as dictionary
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM projects WHERE project_id = ?", (project_id, )).fetchone() 
        return result

def retrieve_project_id(project_name):
    # returns project_id
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return str(cur.execute('select project_id from projects where project_name = "' + project_name + '"').fetchone()[0])

def retrieve_project_id_from_action(action_id):
    # returns project_id
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return str(cur.execute("SELECT project_id from actions where action_id = ?", (action_id, )).fetchone()[0])

def retrieve_all_projects(user_id):
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM projects WHERE user_id = ?", (user_id, )).fetchall() 
        return result

def delete_project(project_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM projects WHERE project_id = ?", (project_id,))
        con.commit()
        # for loop to delete all actions for project

##### ACTION #####
def insert_action(action_name, description, due_date, project_id, finished):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO actions (action_name, description, due_date, project_id, finished) VALUES (?,?,?,?,?)", (action_name, description, due_date, project_id, finished))
        con.commit()
        return cur.lastrowid
    # TODO: Add update functionality

def retrieve_action_id(action_name, description, due_date, project_id, finished):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute("SELECT action_id FROM actions WHERE action_name = ? AND description = ? AND due_date = ? AND project_id = ? AND finished = ?", (action_name, description, due_date, project_id, finished)).fetchone() 
        return result[0]

def update_action(action_id, action_name, description, due_date, project_id, finished):
    
    with sql.connect("database.db") as con:
        sqlQ = ''' UPDATE actions
              SET action_name = ? ,
                  description = ? ,
                  due_date = ?,
                  project_id = ?,
                  finished = ?
              WHERE action_id = ?'''

        cur = con.cursor()
        cur.execute(sqlQ, (action_name, description, due_date, project_id, finished, action_id))
        con.commit()

def retrieve_all_actions(project_id):
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM actions WHERE project_id = ? ORDER BY date(due_date) ASC", (project_id, )).fetchall() 
        return result

def delete_action(action_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM actions WHERE action_id = ?",(action_id, ))
        con.commit()
