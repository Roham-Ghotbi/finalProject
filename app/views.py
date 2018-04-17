from flask import render_template, redirect, request, session, url_for
from app import app, models, db
from .forms import SignupForm, ActionForm, ProjectForm
# Access the models file to use SQL functions
from .models import *


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session: 
        username = session['username']
        return redirect('/trips')
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        if password == retrieve_password(username):
            session['username'] = username
            session['first_name'] = first_name
            # want to launch a popup but stay @ /login w/o 
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect('index')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupForm = SignupForm()
    if signupForm.validate_on_submit():

        username = signupForm.username.data
        password = signupForm.password.data
        insert_user(username, password)
        return redirect('/index')

    return render_template('signup.html', signupForm=signupForm)

@app.route('/timeline')
def display_user_timeline():
    username = session['username']
    first_name = session['first_name']
    user_id = retrieve_user_id(username)
    projects = retrieve_all_projects(user_id)
    return render_template('timeline.html', first_name=first_name, projects=projects)

@app.route('/project_focus/<value>')
def display_project_focus():
    first_name = session['first_name']
    project_id = retrieve_project_id_from_action(value)
    actions = retrieve_all_actions(project_id)
    project = retrieve_project(project_id)
    return render_template('focus.html', first_name=first_name, actions=actions, action_id=value,  project=project)

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    projectForm = ProjectForm()
    username = session['username']

    if ProjectForm.validate_on_submit():
        user_id = retrieve_user_id(username) 
        project_name = projectForm.project_name.data
        description = tripForm.description.data
        due_date = tripForm.due_date.data
        insert_project(project_name, description, due_date, user_id)

    #     return redirect('/trips')
    # return render_template('create_trip.html', name=username, tripForm=tripForm)

@app.route('/create_action', methods=['GET', 'POST'])
def create_action():
    actionForm = ActionForm()
    if ActionForm.validate_on_submit():
        action_name = actionForm.action_name.data
        description = tripForm.description.data
        due_date = tripForm.due_date.data
        # how to get project id
        insert_action(action_name, description, due_date, project_id)

@app.route('/remove_action/<value>')
def remove_action(value):
    delete_action(value)
    # TODO: just want to remove element from DOM w/o redirecting
    return redirect('timeline')


@app.route('/remove_project/<value>')
def remove_project(value):
    delete_project(value)
    # TODO: just want to remove element from DOM w/o redirecting
    return redirect('timeline')

