from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

from flask_login import login_required, current_user
from cinema import db
from cinema.models import Movie
from cinema.posts.forms import MoviePostForm, ScheduleForm, EditMovieForm

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


@login_required
@movies.route("/movies/new_schedule", methods=['GET', 'POST'])
def new_schedule():
    form = ScheduleForm()

    if form.validate_on_submit():
        # schedule will be added to database
        flash("Schedule has been Added.")
        return render_template('new_schedule.html', form=form)
