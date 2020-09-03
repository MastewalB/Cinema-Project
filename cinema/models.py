from datetime import datetime
from flask_login import UserMixin
from cinema import db
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String)
    title = db.Column(db.String(50), nullable=False)
    cover_image = db.Column(db.String(20), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float)
    trailer = db.Column(db.String)
    genres = db.Column(db.String)
    language = db.Column(db.String)
    plot = db.Column(db.Text)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120),  unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    role = db.relationship('role', backref='user', lazy=True)


class Role(db.Model):
    id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.String(15))


class Auditorium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    three_d = db.Column(db.Boolean(), nullable=False)


class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.Integer, nullable=False)
    column = db.Column(db.Integer, nullable=False)
    auditorium_id = db.Column(db.Integer, db.ForeignKey(
        'auditorium.id'), nullable=False)


class Screening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    auditorium_id = db.Column(db.datetime, nullable=False)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    screening_id = db.Column(db.Integer, db.ForeignKey('screening.id'))
    reservation_type = db.Column(
        db.Enum('standard', 'vip', name="reservation_type"))
    # employee that gives the ticket and accepts the moeny
    ticketer = db.Column(db.Integer, db.ForeignKey('user.id'))
    # check if the ticket has expired or not
    active = db.Column(db.Boolean, nullable=True)


class SeatReserved(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'))
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'))
    screening_id = db.Column(db.Integer, db.ForeignKey('screening.id'))
