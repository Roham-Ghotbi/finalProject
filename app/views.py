from __future__ import print_function # In python 2.7
import sys
from flask import render_template, redirect, request, session, url_for
from app import app, models, db
from .forms import SignupForm, ActionForm, ProjectForm
# Access the models file to use SQL functions
from .models import *
#Securing password Storage
import hashlib, uuid

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session: 
        username = session['username']
        ## TODO: this doesn't seem right
        return redirect('/timeline')
    else:
        return render_template('login1.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        username = request.form['username']
        password = hashPass(username, request.form['password'])
        
        if password == retrieve_password(username):
            user = retrieve_user(username)
            session['username'] = username
            session['first_name'] = user['first_name']
            # want to launch a popup but stay @ /login w/o 
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    session.pop('first_name', None)
    return redirect('index')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupForm = SignupForm()
    if signupForm.validate_on_submit():

        first_name = signupForm.first_name.data
        last_name = signupForm.last_name.data
        username = signupForm.username.data
        password = signupForm.password.data
        res = insert_user(username, first_name, last_name, password)
        if res == -1:
            return redirect('/timeline', userExist=True)
        else:
            return redirect('/index')

    return render_template('signup1.html', signupForm=signupForm)

@app.route('/timeline')
def display_user_timeline():
    user_id = retrieve_user_id(session['username'])
    projects = retrieve_all_projects(user_id)
    p = []
    for project in projects:
        project = dict(project)
        project['actions'] = retrieve_all_actions(project['project_id'])
        p += [project]
    print(p, file=sys.stderr)
    return render_template('timeline.html', first_name=session['first_name'], p=p)


@app.route('/project_focus/<value>')
def project_focus(value):
    # TODO: make routing more intuitive, maybe something like /<project_name>/<focus_value>
    # TODO: use value to focus on action
    project_id = retrieve_project_id(value)
    actions = retrieve_all_actions(project_id)
    project = retrieve_project(project_id)
    return render_template('focus.html', first_name=session['first_name'], actions=actions, action_id=value,  project=project)

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    projectForm = ProjectForm()
    username = session['username']
    if projectForm.validate_on_submit():
        user_id = retrieve_user_id(username) 
        project_name = projectForm.project_name.data
        description = projectForm.description.data
        due_date = projectForm.due_date.data
        insert_project(project_name, description, due_date, user_id)
        return redirect('/timeline')
    return render_template('create_project.html', first_name=session['first_name'], projectForm=projectForm)

# @app.route('/create_action', methods=['GET', 'POST'])
# def create_action():
#     actionForm = ActionForm()
#     if actionForm.validate_on_submit():
#         action_name = actionForm.action_name.data
#         description = actionForm.description.data
#         due_date = actionForm.due_date.data
#         project_name = actionForm.project_name.data
#         # TODO: how to get project id from project I am clicking from
#         project_id = retrieve_project_id(project_name)
#         project = retrieve_project(project_id)
#         action_id = insert_action(action_name, description, due_date, project_id)
#         # actions = 
#         return render_template('focus.html', first_name=session['first_name'], actions=actions, action_id=action_id,  project=project)
#    return render_template('create_action.html', actionForm=actionForm)

@app.route('/create_action', methods=['GET', 'POST'])
def create_action():
    actionForm = ActionForm()
    if actionForm.validate_on_submit():
        action_name = actionForm.action_name.data
        description = actionForm.description.data
        due_date = actionForm.due_date.data
        project_name = actionForm.project_name.data
        # TODO: how to get project id from project I am clicking from
        project_id = retrieve_project_id(project_name)
        insert_action(action_name, description, due_date, project_id)
        return redirect('/timeline')
    return render_template('create_action.html', first_name=session['first_name'], actionForm=actionForm)

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




