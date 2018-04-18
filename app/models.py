import sqlite3 as sql

# user functions

def insert_user(username, first_name, last_name, password):
    # returns user_id
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, first_name, last_name, password) VALUES (?,?)", (username, first_name, last_name, password))
        con.commit()
        return cur.lastrowid

def retrieve_user_id(username):
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	return str(cur.execute('select user_id from users where username = "' + username + '"').fetchone()[0]) # why is it in tuple form??

def retrieve_all_emails():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return cur.execute('select username from users').fetchall()

def retrieve_password(username):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return str(cur.execute('SELECT password from users where username = "' + username +'"').fetchone()[0])
# trip functions

def insert_project(project_name, description, due_date, user_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO projects (project_name, description, due_date, user_id) VALUES (?,?,?,?)", (project_name, description, due_date, user_id))
        con.commit()
    # TO DO: Add update functionality

def retrieve_project(project_id):
    # returns project as a dictionary
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute('select * from projects where project_id = "' + project_id + '"').fetchone()[0]
        return result

def retrieve_all_projects(user_id):
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute('select * from projects where user_id = "' + user_id + '"').fetchall() 
        return result

def delete_project(project_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE from projects where project_id = " + project_id)
        con.commit()
        # for loop to delete all actions for project

##### ACTION #####
def insert_action(action_name, description, due_date, project_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO actions (action_name, description, due_date, project_id) VALUES (?,?,?,?)", (action_name, description, due_date, project_id))
        con.commit()
    # TO DO: Add update functionality

def retrieve_project_id_from_action(action_id):
    # returns project_id
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return str(cur.execute('select project_id from actions where action_id_"' + action_id + '"').fetchone()[0])

# def retrieve_project(project_name, uid):
#     # returns project_id
#     with sql.connect("database.db") as con:
#         cur = con.cursor()
#         return str(cur.execute('select project_id from users where project_name = "' + project_name + '" and user_id = "' + uid + '"').fetchone()[0])


def retrieve_all_actions(project_id):
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute('select * from actions where project_id = "' + project_id + '"').fetchall() 
        return result

def delete_action(action_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE from actions where action_id = " + action_id)
        con.commit()
