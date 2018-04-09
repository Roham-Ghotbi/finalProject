from flask import render_template, redirect, request, session, url_for
from app import app, models, db
from .forms import SignupForm, TripForm
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

@app.route('/user')
def display_user():
    username = session['username']
    uid = retrieve_user(username)
    return render_template('user.html', uid=uid, name=username)

@app.route('/trips')
def display_trips():
    username = session['username']
    trips = retrieve_trips(username)
    return render_template('trips.html', name=username, trips=trips)

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    tripForm = TripForm()
    username = session['username']

    if tripForm.validate_on_submit():
        owner_id = retrieve_user(username) 
        trip_name = tripForm.trip_name.data
        destination = tripForm.destination.data
        friend_username = tripForm.friend_username.data
        friend_id = retrieve_user(friend_username)
        insert_trip(trip_name, destination, owner_id, friend_id)
        return redirect('/trips')
    return render_template('create_trip.html', name=username, tripForm=tripForm)

@app.route('/remove_trip/<value>')
def remove_trip(value):
    delete_trip(value)
    
    # TODO: just want to remove element from DOM w/o redirecting
    return redirect('trips')


