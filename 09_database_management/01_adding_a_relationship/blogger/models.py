from flask_sqlalchemy import SQLAlchemy
import datetime
from blogger import app

db = SQLAlchemy(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)
    dateofreg = db.Column(db.DateTime, default=datetime.datetime.now)
    post_id = db.relationship("Post", backref="user", lazy="dynamic")

    #post_id = db.Column(db.Integer, db.ForeignKey("posts.pid"))

    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email


class Post(db.Model):
    __tablename__ = 'posts'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey("users.uid"))

    #puid = db.Column(db.Integer, db.ForeignKey('users.uid'))

    def __init__(self, title, description, puid):
        self.title = title
        self.description = description
        self.puid = puid


db.create_all()
