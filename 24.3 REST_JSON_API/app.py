"""Flask app for Cupcakes"""

from flask import Flask, request, render_template,  redirect, flash, session, jsonify
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

# Create serialize function for json 
def serialize_cupcake(cupcake):
    """Returns dict representation of cupcakes to turn into JSON"""

    return {
        'id': cupcake.id,
        'flavor': cupcake.flavor,
        'size': cupcake.size,
        'rating': cupcake.rating,
        'image': cupcake.image
    }
    
@app.route('/')
def homepage():
    """Shows homepage"""
    return render_template('base.html')

@app.route('/api/cupcakes')
def get_all_cupcakes():
    """Shows list of all cupcakes in db"""
    cupcakes = Cupcake.query.all()
    serialize = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialize)

@app.route('/api/cupcakes/<int:c_id>')
def get_single_cupcakes(c_id):
    """Shows list of single cupcake in db"""
    cupcake = Cupcake.query.get(c_id)
    serialize = serialize_cupcake(cupcake)

    return jsonify(cupcakes=serialize)

@app.route('/api/cupcakes', methods=["POST"])
def new_cupcake():
    """Add a new cupcake to db"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating=request.json["rating"]
    image = request.json["image"]
    
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    
    db.session.add(new_cupcake)
    db.session.commit()

    seralize = serialize_cupcake(new_cupcake)
    return (jsonify(cupcake=seralize), 201)

@app.route('/api/cupcakes/<int:cc_id>', methods=["PATCH"])
def edit_cupcake(cc_id):
    """Edit existing cupcake"""
    cupcake = Cupcake.query.get_or_404(cc_id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake=serialize_cupcake(cupcake))

@app.route('/api/cupcakes/<int:cc_id>', methods=["DELETE"])
def delete_cupcake(cc_id):
    """Delete particular cupcake"""
    cupcake = Cupcake.query.get_or_404(cc_id)

    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted cupcake")
