from flask.ext.wtf import Form
from wtforms import StringField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

# class LoginForm(Form):
#     username = StringField('username', validators=[DataRequired()])
#     password = StringField('password', validators=[DataRequired()])

class SignupForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    
class TripForm(Form):
    trip_name = StringField('trip_name', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend_username = StringField('friend_username', validators=[DataRequired()])