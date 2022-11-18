from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db




auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get("password1")
        password2=request.form.get("password2")

        if len(email)<4:
            flash('Email needs to longer than 4 characters', category="error")
        elif len(name)<5:
            flash("name is too short", category='error')
        elif len(password1)<8 or len(password1)>16:
            flash("Password must be longer than 8 and no longer than 16 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password1, Method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Welcome to the PowerLift family!", category="success")
            return redirect(url_for('views.home'))
    return render_template("login.html", boolean=True)

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    data=request.form
    print(data)
    return render_template("signup.html")