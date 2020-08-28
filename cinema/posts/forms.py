from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DecimalField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

#this form is used to add a new Movie
#? How to add movie trailer and rating?

class MoviePostForm(FlaskForm):
    movie_title = ('Movie Title', validators=[DataRequired()])
    cover_image = FileField('Enter Movie Cover', validators=[FileAllowed(['jpg','png'])])
    genres = StringField('Genres', validators=[DataRequired()])
    
    submit = SubmitField('Add')

class EditMovieForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    cover_image = FileField( 'Cover Image', validators=[FileAllowed(['jpg','png'])] )
    rating = DecimalField('rating', validators=[DataRequired()])
    
    trailer = FileField( 'movie trailer', validators=[FileAllowed(['mp4','mkv'])] )
    genres = StringField('genres', validators=[DataRequired()])
    language = StringField('language', validators=[DataRequired()])
    plot = TextField('plot', validators=[DataRequired()])
