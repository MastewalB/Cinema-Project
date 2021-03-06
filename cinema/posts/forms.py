from flask_wtf import FlaskForm
from wtforms import DateTimeField, StringField, SubmitField, TextAreaField, DecimalField, IntegerField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

# this form is used to add a new Movie
# ? How to add movie trailer and rating?
# This is for sample will be re-arranged
LANGUAGE_CHOICES = ['English', 'Amharic']
# Class not finished


class MoviePostForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    cover_image = FileField('Enter Movie Cover',
                            validators=[FileAllowed(['jpg', 'png'])])
    genres = StringField('Genres', validators=[DataRequired()])
    trailer = StringField('Trailer')
    plot = TextAreaField('Plot')
    language = SelectField('Language', choices=LANGUAGE_CHOICES)

    submit = SubmitField('Add')


class SearchForm(FlaskForm):
    title = StringField('Enter the title', validators=[DataRequired()])
    submit = SubmitField('Search')


class EditMovieForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    cover_image = FileField('Cover Image', validators=[
                            FileAllowed(['jpg', 'png'])])
    rating = DecimalField('rating', places=1, validators=[DataRequired()])

    trailer = FileField('movie trailer', validators=[
                        FileAllowed(['mp4', 'mkv'])])
    genres = StringField('genres', validators=[DataRequired()])
    language = StringField('language', validators=[DataRequired()])
    plot = TextAreaField('plot', validators=[DataRequired()])

    submit = SubmitField('Save Edit')


class ScheduleForm(FlaskForm):
    movie = SelectField('Select Movie', choices=[])
    schedule = DateTimeField(
        'Pick a Date', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])

    auditorium = SelectField('Select Auditorium', choices=[])
    submit = SubmitField("Save Schedule")
