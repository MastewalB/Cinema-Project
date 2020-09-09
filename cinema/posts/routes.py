from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

from flask_login import login_required, current_user
from cinema import db
from cinema.models import Movie
from cinema.posts.forms import MoviePostForm, ScheduleForm, EditMovieForm, SearchForm

movies = Blueprint('movies', __name__)


@movies.route("/movies/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = MoviePostForm()
    if form.validate_on_submit():
        post = Movie(title=form.title.data, cover_image=form.cover_image.data, rating=form.rating.data, trailer=form.trailer.data, genres=form.genres.data,
                     language=form.language.data)
        db.session.add(post)
        db.session.commit()
        flash('Movie succesfully Added to the Database', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@movies.route("/movies/new/from_imdb", methods=['GET', 'POST'])
@login_required
def new_from_imdb():
    form = SearchForm()
    if form.validate_on_submit:
        #! Need to be checked
        url = "https://imdb8.p.rapidapi.com/title/auto-complete"
        querystring = form.title.data
        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "f2e812830cmsh9729566b770101fp17a9afjsn1fc425f4ade5"
        }
        # the request returns a JSON file that contains search results of the movie
        response = request.request(
            "GET", url, headers=headers, params=querystring)


@login_required
@movies.route("/movies/new_schedule", methods=['GET', 'POST'])
def new_schedule():
    form = ScheduleForm()
    #! this query selects all movies from databases
    form.movie.choices = [(movie.id, movie.name)
                          for movie in Movie.query.all()]
    form.auditorium.choices = [(auditorium.id, auditorium.name)
                               for auditorium in Auditorium.query.all()]
    if form.validate_on_submit():
        # schedule will be added to database
        flash("Schedule has been Added.")
        return render_template('new_schedule.html', form=form)
