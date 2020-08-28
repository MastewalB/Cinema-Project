from datetime import datetime
from flask_login import UserMixin
from cinema import db
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Movie(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    imdb_id = db.Column( db.String)
    title = db.Column( db.String(50), nullable=False )
    cover_image = db.Column( db.String(20), nullable=False )
    rating = db.Column( db.Float )
    trailer = db.Column( db.String )
    genres = db.Column( db.String )
    language = db.Column( db.String )
    plot = db.Column(db.Text)


class User(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String(40), nullable=False)
    email = db.Column( db.String(120),  unique=True, nullable=False )
    username = db.Column( db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    role = db.relationship('role', backref='user', lazy=True)


class Role(db.Model):
    id = db.Column( db.Integer(), db.ForeignKey('user.id'), nullable=False)
    role = db.Column( db.String(15))


class Cinema(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String(100), nullable=False )
    size = db.Column( db.String(5), nullable=False )
    three_d = db.Column( db.Boolean(), nullable=False )
