# Import others when you use them
from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request
import cinema
from cinema.users import db
from cinema.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from ..models import User
from flask_login import login_user, current_user, logout_user, login_required

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = User(username=form.username.data, email=form.email.data, gender=form.gender.data)

        password = User(password=form.password.data)
        db.add(password)
        db.commit()

        flash('Your account has been created!, wait till you get the confirmation code')
        return redirect(url_for('login'))
        return render_template('register.html', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        passwd = User.query.filter_by(password=form.password.data).first()
        if user and passwd:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))

        else:
            flash('Login Unsuccessful. Please check Email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@users.route("/developer", methods=['GET', 'POST'])
def developer():
    developer_mssg = register.username
    db.session.add(developer_mssg)
    db.commit()
    flash("you added a user!")
    return render_template('developer.html', title='developer')


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            from cinema.users.utils import save_picture
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)
