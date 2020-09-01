from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

from flask_login import login_required, current_user
#from cinema.models import Movie
from cinema import db
from cinema.models import Movie
from cinema.posts.forms import MoviePostForm

movies = Blueprint('movies', __name__)


@movies.route("/movices/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form =MoviePostForm()
    if form.validate_on_submit():
        post = Movie(title = form.title.data ,cover_image =form.cover_image.data,rating =form.rating.data, trailer =form.trailer.data,genres=form.genres.data,
                     language =form.language.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')