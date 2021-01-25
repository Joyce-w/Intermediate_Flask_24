from flask_sqlalchemy import SQLAlchemy

# initalize SQLA 
db = SQLAlchemy()

#connect app with SQLA instance
#call logic to connect to db from app.py, don't want to happen everytime models.py is ran
def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    #Determine table name
    __tablename__ = "pets"

    def __repr__(self):
        p=self
        return f"<Pet id={p.id} name={p.name} species={p.species} photo_url = {p.photo_url}, age = {p.age}, notes = {p.notes}, available = {p.available}>"


    #define individual col in pet table
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)

    
    name = db.Column(db.String(30),
                    nullable=True)
    
    species = db.Column(db.String(30),
                    nullable=True)
    
    photo_url = db.Column(db.String)
    
    age = db.Column(db.Integer)
    
    notes= db.Column(db.String)
    
    available = db.Column(db.Boolean,
                    nullable=True,
                    default=True)
