"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

# initalize SQLA 
db = SQLAlchemy()

#connect app with SQLA instance
#call logic to connect to db from app.py, don't want to happen everytime models.py is ran
def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW
class Cupcake(db.Model):
    #special dunder method to determine table name
    __tablename__ = "cupcakes"


    #define individual col in pet table
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)

    #nullable = opposite of not null, SQLA default will be NULL 
    flavor = db.Column(db.String(20),
                    nullable=True,)
    
    size = db.Column(db.String(10),
                    nullable=True)
    
    rating = db.Column(db.Float(10),
                    nullable=True)
    
    image = db.Column(db.String,
                    nullable=False,
                    default='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')

