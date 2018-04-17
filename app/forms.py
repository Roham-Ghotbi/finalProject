from flask.ext.wtf import Form
from wtforms import StringField, DateField
from wtforms.validators import DataRequired

# class LoginForm(Form):
#     username = StringField('username', validators=[DataRequired()])
#     password = StringField('password', validators=[DataRequired()])

class SignupForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    
class ActionForm(Form):
    action_name = StringField('action_name', validators=[DataRequired()])
    description = StringField('description')
    due_date = DateField('due_date')

class ProjectForm(Form):
    project_name = StringField('action_name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    due_date = DateField('due_date')