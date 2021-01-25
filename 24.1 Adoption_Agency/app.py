from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


# app created 
app = Flask(__name__)

# specify that youre using postgres and a specific database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#call connect_db from models
connect_db(app)
    
@app.route('/')
def homepage():
    """homepage, render pet information"""
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add new pet to adoption"""
    form = AddPetForm()
    if form.validate_on_submit():
        flash('Pet registered!')
        #make new model
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        is_available = form.available.data

        pet = Pet(name=name, species=species,photo_url=photo_url, age=age, notes=notes,available=is_available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)
