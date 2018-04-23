from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.fields.html5 import DateField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired, Optional, Email

# TODO: Enable optional input

class LoginForm(Form):
	username = EmailField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])

class SignupForm(Form):
	first_name = StringField('first_name', validators=[DataRequired()])
	last_name = StringField('last_name', validators=[DataRequired()])
	username = EmailField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])
    
class ActionForm(Form):
    action_name = StringField('action_name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    due_date = DateField('due_date', validators=[DataRequired()])

class ProjectForm(Form):
    project_name = StringField('action_name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    due_date = DateField('due_date', validators=[Optional()])