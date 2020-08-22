from datetime import datetime
from flask_login import UserMixin
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer




class Movie(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    title = db.Column( db.String(50), nullable=False )
    description = db.Column( db.String(100), nullable=False )
    cover_image = db.Column( db.String(20), nullable=False )
    imdb_rating = db.Column( db.Integer )
    genres = db.Column( db.String(50), nullable=False )
