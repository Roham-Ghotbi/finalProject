from __future__ import print_function # In python 2.7
import sys
from flask import render_template, redirect, request, session, url_for
import models
# Access the models file to use SQL functions
#Securing password Storage
import hashlib, uuid

res = models.retrieve_action_id(action_name="Buy Lumber", description="Updated", due_date="0011-11-11", project_id=1, finished="0")

models.update_action(action_id=res, action_name="Buy Lumber", description="Updated", due_date="0011-11-11", project_id=1, finished="1")