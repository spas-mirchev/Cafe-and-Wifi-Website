from flask import render_template, redirect, flash, url_for, request
from flaskcafe.models import Cafe, Users
from flaskcafe import app
from flaskcafe import db
from flaskcafe.forms import CafeForm, RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required, logout_user
import json
import re


@app.route("/", methods=['GET', 'POST'])
def home():
    arg1 = request.args.get('has_wifi', default=None)
    arg2 = request.args.get('has_sockets', None)
    arg3 = request.args.get('has_toilet', None)
    arg4 = request.args.get('can_take_calls', None)
    cafes = Cafe.query.all()
    enhanced_cafes = []
    for cafe in cafes:
        coordinates = re.search(
            '[-?\d\.]*\,([-?\d\.]*)', cafe.map_url).group().split(',')
        enhanced_cafes.append(
            {"cafe": cafe, "coordinates": json.dumps(coordinates)})

    return render_template("index.html", enhanced_cafes=enhanced_cafes, logged_in=current_user.is_authenticated, arg1=arg1, arg2=arg2, arg3=arg3, arg4=arg4)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.", 'warning')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Invalid password provided', 'warning')
            return redirect(url_for('login'))
        else:
            login_user(user)
            flash(f'Hi {current_user.username}', 'success')
            return redirect(url_for('home'))

    return render_template("login.html", title='Login', form=form, logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        user = Users(username=form.username.data,
                     email=form.email.data, password=hash_and_salted_password)
        db.session.add(user)
        db.session.commit()
        flash('Welcome', 'info')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form, logged_in=current_user.is_authenticated)


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(name=form.name.data, map_url=form.map_url.data, img_url=form.img_url.data, location=form.location.data, has_sockets=form.has_sockets.data, has_toilet=form.has_toilet.data, has_wifi=form.has_wifi.data,
                        can_take_calls=form.can_take_calls.data, seats=form.seats.data, coffee_price=form.coffee_price.data)
        db.session.add(new_cafe)
        db.session.commit()
        flash('New cafe has been added', 'info')
        return redirect(url_for('home'))
    return render_template("admin.html", form=form, title='Admin block', logged_in=current_user.is_authenticated)


@app.route("/all-cafes/", methods=['GET', 'POST'])
def all_cafes():
    cafes = Cafe.query.all() 
    
    return render_template("all_cafes.html", cafes=cafes)

@app.route("/delete/<int:cafe>")
def delete_post(cafe):
    post_to_delete = Cafe.query.get(cafe)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out', 'info')
    return redirect(url_for('home'))
