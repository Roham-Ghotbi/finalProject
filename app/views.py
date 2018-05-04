from __future__ import print_function # In python 2.7
import sys
from flask import render_template, redirect, request, session, url_for, json
from app import app, models, db
from .forms import SignupForm, ActionForm, ProjectForm, EditForm
# Access the models file to use SQL functions
from .models import *
#Securing password Storage
import hashlib, uuid
import datetime

#the index page
#if a user is already signed in, it will load its timeline, otherwise it will go to the login page
@app.route('/')
@app.route('/index')
def index():
    if 'username' in session: 
        username = session['username']
        return redirect('/timeline')
    else:
        return render_template('login.html')

#the login page
#getting the user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        username = request.form['username']
        password = hashPass(username, request.form['password'])
        
        if retrieve_password(username) is not None and password == retrieve_password(username):
            user = retrieve_user(username)
            session['username'] = username
            session['first_name'] = user['first_name']
        else:
            return render_template('login.html', message="Incorrect Password or Username(Email)")

    return redirect(url_for('index'))

#logging out the user from the website
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    session.pop('first_name', None)
    return redirect('index')


#signup page for new users
#accesible through login page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        if retrieve_user(username) is not None:
            return render_template('/signup.html', message="Username Already Exists!")
        elif username == "" or password == "" or first_name == "" or last_name == "":
            return render_template('/signup.html', message="Please Fill out the form Completely!")
        else:
            res = insert_user(username, first_name, last_name, password)
            session['username'] = username
            session['first_name'] = first_name
            return redirect(url_for('index'))

    return render_template('signup.html')


#timeline 
#core of our website
#will only be loaded if a user is signed in
#will go to the login page otherwise
@app.route('/timeline')
def display_user_timeline():
    if 'username' in session:
        user_id = retrieve_user_id(session['username'])
        projects = retrieve_all_projects(user_id)
        p = []
        for project in projects:
            project = dict(project)
            project['actions'] = retrieve_all_actions(project['project_id'])
            p += [project]

        projectForm = ProjectForm()
        actionForm = ActionForm()
        editForm = EditForm()
        return render_template('timeline.html', first_name=session['first_name'], p=p, projectForm=projectForm, actionForm=actionForm, editForm=editForm)
    else:
        return render_template('login.html')


@app.route('/project_focus/<value>')
def project_focus(value):
    project_id = retrieve_project_id(value)
    actions = retrieve_all_actions(project_id)
    project = retrieve_project(project_id)
    return render_template('focus.html', first_name=session['first_name'], actions=actions, action_id=value,  project=project)

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    colors = ["red", "blue", "green", "yellow", "purple", "cyan"]
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if 'username' in session:
        projectForm = ProjectForm()
        username = session['username']
        if projectForm.is_submitted():
            user_id = retrieve_user_id(username) 
            project_name = projectForm.project_name.data
            description = projectForm.description.data
            due_date = projectForm.due_date.data
            color = projectForm.color.data

            if project_name == "": 
                project_name = "MyProject"
            if description == "": 
                description = "Description"
            if due_date is None: 
                due_date = datetime.date(year, month, day)
            if color == "" or color not in colors:
                color = "blue"

            insert_project(project_name, description, due_date, color, user_id)

        return redirect('/timeline')

    else:
        return render_template('login.html')

@app.route('/create_action', methods=['GET', 'POST'])
def create_action():
    #creating the action based on the user input
    #using default values otherwise
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if 'username' in session:
        actionForm = ActionForm()
        if actionForm.is_submitted():
            action_name = actionForm.action_name.data
            description = actionForm.description.data
            due_date = actionForm.due_date.data
            project_name = actionForm.project_name.data
            project_id = retrieve_project_id(project_name)
            color = retrieve_project(project_id)['color']

            if action_name == "": 
                action_name = "MyAction"
            if description == "": 
                description = "Description"
            if due_date is None: 
                due_date = datetime.date(year, month, day)

            insert_action(action_name, description, due_date, project_id, color, finished=0)
            
        return redirect('/timeline')
    else:
        return render_template('login.html')

#deletingan action of a project
@app.route('/remove_action/<value>')
def remove_action(value):
    delete_action(value)
    return redirect('timeline')

#updating an action of a project
@app.route('/edit_action/<value>', methods=['GET', 'POST'])
def edit_action(value):
    if 'username' in session:
        #getting data in the db
        action = retrieve_action(value)
        
        #basically updating whatever new data the user puts in
        #and keeping the unchanged ones intact
        editForm = EditForm()
        if editForm.is_submitted():
            action_name = editForm.action_name.data
            description = editForm.description.data
            due_date = editForm.due_date.data

            if action_name == "": 
                action_name = action['action_name']
            if description == "": 
                description = action['description']
            if due_date is None: 
                due_date = action['due_date']  

            update_action(action['action_id'], action_name, description, due_date, action['project_id'], action['color'], action['finished'])
            
        return redirect('/timeline')
    else:
        return render_template('login.html')

@app.route('/remove_project/<value>', methods=["GET"])
def remove_project(value):
    delete_project(value)
    return redirect('timeline')

@app.route('/toggle_done', methods=['GET','POST'])
def toggle_done():
    action_id = request.form['action_id']
    update_done(action_id)
    return json.dumps({})

@app.route('/toggle_not_done', methods=['GET','POST'])
def toggle_not_done():
    action_id = request.form['action_id']
    update_not_done(action_id)
    return json.dumps({})

