from flask import Flask
#regex module
import re

app = Flask(__name__)

#used for session
app.secret_key = "password123"
#global reference to DB name
DATABASE = "ownershipHistory"
#create a regular expression
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')