"""Flask app for Cupcakes"""

from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake


# app created 
app = Flask(__name__)

# specify that youre using postgres and a specific database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Whats_the_secret_1262021"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#call connect_db from models
connect_db(app)
    
@app.route('/')
def homepage():
    """Shows list of all pets in db"""
    return render_template('base.html')