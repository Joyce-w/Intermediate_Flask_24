"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
momo = Pet(name='Momo', species="dog")
stripes = Pet(name='Stripes', species="raccoon", age=4)
butters = Pet(name='Butters', species="chicken", photo_url="https://www.thehappychickencoop.com/wp-content/uploads/2017/10/Silkie-Chicken.png", notes="Likes to say bokbokbok")
shadow = Pet(name='Shadow', species="dog", photo_url="https://www.dogtime.com/assets/uploads/2019/05/alaskan-malamute-puppy-1-1280x720.jpg", notes="henlo bork bork", age=2)


# Add new objects to session, so they'll persist
db.session.add(momo)
db.session.add(stripes)
db.session.add(butters)
db.session.add(shadow)

# Commit--otherwise, this never gets saved!
db.session.commit()
