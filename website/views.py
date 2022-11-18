from flask import Blueprint, render_template



views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", image_flie="website\static\logopowerlift.jpg")

@views.route('/login')
def home():
    return render_template("login.html")

@views.route('/signup')
def home():
    return render_template("signup.html")

@views.route('/')
def home():
    return render_template("/")

