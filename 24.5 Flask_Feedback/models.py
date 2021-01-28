from flask_sqlalchemy import SQLAlchemy

# initalize SQLA 
db = SQLAlchemy()

#connect app with SQLA instance
#call logic to connect to db from app.py, don't want to happen everytime models.py is ran
def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(20),
                    primary_key=True)
                    
    password = db.Column(db.String,
                    nullable=False)

    email = db.Column(db.String(50),
                    nullable=False,
                    unique=True)

    first_name = db.Column(db.String(30),
                    nullable=False)

    last_name = db.Column(db.String(30),
                    nullable=False)
