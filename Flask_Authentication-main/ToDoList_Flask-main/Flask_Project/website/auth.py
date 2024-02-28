from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user, LoginManager


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        print(email)
        print(password)

        user = User.query.filter_by(email=email).first()
        print(user)

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember = remember)
                return redirect(url_for('views.profile'))
            else:
                flash(f'Incorrect password, try again.', category ='error')
        else:
            flash('Email does not exist.', category ='error')
    return render_template("login.html", name=current_user)

@auth.route("/logout")
@login_required
def logout():
    flash("You have been logged out.", "info")
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #code to validate and add user to database goes here
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='exist_error')
            return render_template("signup.html", name=current_user)
        else:
            # create a new user with the form data. Hash the password so the plaintext version isn't saved.
            new_user = User(email=email, name=name, password=generate_password_hash(password))

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return render_template("signup.html")

    return render_template("signup.html", name=current_user)