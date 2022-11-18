from flask import Blueprint, render_template, request



views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", image_flie="website\static\logopowerlift.jpg")


@views.route('/cart')
def cart():
    return render_template("cart.html")

