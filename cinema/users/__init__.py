from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY'] = 'c4807a65e59a6278c66046b02e7ec155'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from cinema.users import routes