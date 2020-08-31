from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

from flask_login import login_required, current_user
#from cinema.models import Movie
from cinema.posts.forms import MoviePostForm

movies = Blueprint('movies', __name__)

@movies.route("/movies/new", methods=['GET', 'POST'])
@login_required #? Admins only
def new_movie():
    form = MoviePostForm()

    return 
    
