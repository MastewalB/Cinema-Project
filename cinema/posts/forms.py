from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

#this form is used to add a new Movie
#? How to add movie trailer and rating?

class MoviePostForm(FlaskForm):
    movie_title = ('Movie Title', validators=[DataRequired()])
    cover_image = FileField('Enter Movie Cover', validators=[FileAllowed(['jpg','png'])])
    genres = StringField('Genres', validators=[DataRequired()])
    
    submit = SubmitField('Add')
