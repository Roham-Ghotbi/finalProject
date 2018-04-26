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
	first_name = StringField('first_name', validators=[DataRequired()],  render_kw={"placeholder": "First"})
	last_name = StringField('last_name', validators=[DataRequired()],  render_kw={"placeholder": "Last"})
	username = EmailField('username', validators=[DataRequired()],  render_kw={"placeholder": "Email"})
	password = StringField('password', validators=[DataRequired()],  render_kw={"placeholder": "Password"})
    
class ActionForm(Form):
    action_name = StringField('action_name', validators=[DataRequired()], render_kw={"placeholder": "Action"})
    description = StringField('description', validators=[DataRequired()], render_kw={"placeholder": "Description"})
    project_name = StringField('project_name', validators=[DataRequired()])
    due_date = DateField('due_date', validators=[DataRequired()])

class ProjectForm(Form):
    project_name = StringField('action_name', validators=[DataRequired()], render_kw={"placeholder": "Project Title"})
    description = StringField('description', validators=[DataRequired()], render_kw={"placeholder": "Description"})
    due_date = DateField('due_date', validators=[Optional()],)
    color = StringField('color', validators=[DataRequired()], render_kw={"placeholder": "Color"})
