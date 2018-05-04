import sqlite3 as sql
#Securing password Storage
import hashlib, uuid

##### USERS #####

def hashPass(username, password):
    #hashMethod for securely storing password
    salt = hashlib.sha512(username).hexdigest()
    return hashlib.sha512(password + salt).hexdigest()

def insert_user(username, first_name, last_name, password):
    # returns user_id
    with sql.connect("database.db") as con:
        cur = con.cursor()
       
        password = hashPass(username, password)
        cur.execute("INSERT INTO users (email, first_name, last_name, password) VALUES (?,?,?,?)", (username, first_name, last_name, password))
        con.commit()
        return cur.lastrowid
        
#getting user from DB based on their username(email)
def retrieve_user(username):
    # returns user as a dictionary
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM users WHERE email = ?", (username,)).fetchone()
        return result

#getting usersID from DB based on their username(email)
def retrieve_user_id(username):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute("SELECT user_id FROM users WHERE email = ?", (username, )).fetchone()
        if result is None:
            return None
        else:
            return str(result[0]) 

#getting all the emails from the db
def retrieve_all_emails():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        return cur.execute('SELECT username FROM users').fetchall()

#getting the password(hashed version) from the db
def retrieve_password(username):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute("SELECT password FROM users WHERE email = ?", (username, )).fetchone()
        if result is None:
            return None
        else:
            return str(result[0])

##### Projects #####

#insert a project inside out db for a user
def insert_project(project_name, description, due_date, color, user_id):
    with sql.connect("database.db") as con:
        print(due_date)
        print(type(due_date))
        
        d = due_date
        due_date = d.strftime('%b')  + ' ' + d.strftime('%d').strip("0")
        cur = con.cursor()
        cur.execute("INSERT INTO projects (project_name, description, due_date, color, user_id) VALUES (?,?,?,?,?)", (project_name, description, due_date, color, user_id))
        con.commit()

#getting a project based on its id
def retrieve_project(project_id):
    # returns project as dictionary
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM projects WHERE project_id = ?", (project_id, )).fetchone() 
        return result

#get a projects id
def retrieve_project_id(project_name):
    # returns project_id
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute("SELECT project_id from projects where project_name = ?", (project_name, )).fetchone()
        if result is None:
            return None
        else:
            return str(result[0])

#get a project id of an action
def retrieve_project_id_from_action(action_id):
    # returns project_id
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute("SELECT project_id from actions where action_id = ?", (action_id, )).fetchone()
        if result is None:
            return None
        else:
            return str(result[0])
 
#get all the projects in our db           
def retrieve_all_projects(user_id):
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM projects WHERE user_id = ?", (user_id, )).fetchall() 
        return result

#delete a project from db
def delete_project(project_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM projects WHERE project_id = ?", (project_id,))
        cur.execute("DELETE FROM actions WHERE project_id = ?", (project_id,))
        con.commit()


##### ACTIONS #####

#add an action to a project
def insert_action(action_name, description, due_date, project_id, color, finished):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO actions (action_name, description, due_date, project_id, color, finished) VALUES (?,?,?,?,?,?)", (action_name, description, due_date, project_id, color, finished))
        con.commit()
        return cur.lastrowid

#get an action id
def retrieve_action_id(action_name, description, due_date, project_id, finished):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute("SELECT action_id FROM actions WHERE action_name = ? AND description = ? AND due_date = ? AND project_id = ? AND finished = ?", (action_name, description, due_date, project_id, finished)).fetchone() 
        if result is None:
            return None
        else:
            return result[0]

#update an already existing action
def update_action(action_id, action_name, description, due_date, project_id, color, finished):
    
    with sql.connect("database.db") as con:
        sqlQ = ''' UPDATE actions
              SET action_name = ? ,
                  description = ? ,
                  due_date = ?,
                  project_id = ?,
                  color = ?,
                  finished = ?
              WHERE action_id = ?'''

        cur = con.cursor()
        cur.execute(sqlQ, (action_name, description, due_date, project_id, color, finished, action_id))
        con.commit()

#updating the state of an action to be done
def update_done(action_id):
    
    with sql.connect("database.db") as con:
        sqlQ = ''' UPDATE actions
              SET finished = ?
              WHERE action_id = ?'''

        cur = con.cursor()
        cur.execute(sqlQ, (True, action_id))
        con.commit()

#updating the state of an action to be not done
def update_not_done(action_id):
    
    with sql.connect("database.db") as con:
        sqlQ = ''' UPDATE actions
              SET finished = ?
              WHERE action_id = ?'''

        cur = con.cursor()
        cur.execute(sqlQ, (False, action_id))
        con.commit()

#Get all the actions of a project
def retrieve_all_actions(project_id):
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM actions WHERE project_id = ? ORDER BY date(due_date) ASC", (project_id, )).fetchall() 
        return result

#get an action based on its id
def retrieve_action(action_id):
    # returns action as dictionary
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM actions WHERE action_id = ?", (action_id, )).fetchone() 
        return result

#remove an action from a project
def delete_action(action_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM actions WHERE action_id = ?",(action_id, ))
        con.commit()
