from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initalize SQLA 
db = SQLAlchemy()

bcrypt = Bcrypt()

#connect app with SQLA instance
#call logic to connect to db from app.py, don't want to happen everytime models.py is ran
def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True,
                    autoincrement=True)

    username = db.Column(db.String(20))
    
    password = db.Column(db.String,
                    nullable=False)

    email = db.Column(db.String(50),
                    nullable=False,
                    unique=True)

    first_name = db.Column(db.String(30),
                    nullable=False)

    last_name = db.Column(db.String(30),
                    nullable=False)

    @classmethod
    def register(cls, username, pwd):
        """Register user w/ hashed pw"""
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf")

        return cls(username=username, password=hashed_utf8)

    @classmethod
    def authenticate(cls, username, pwd):
        """validate login user"""
        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False