from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User


# app created 
app = Flask(__name__)

# specify that youre using postgres and a specific database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretsecret1282021"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#call connect_db from models
connect_db(app)

@app.route('/')
def homepage():
    """show homepage"""

    return redirect('/register')

@app.route('/register')
def register():
    """Registeration form for new user"""

    return render_template('register.html')
