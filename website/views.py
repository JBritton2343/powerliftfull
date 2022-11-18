from flask import Blueprint, render_template, request
from flask_login import  login_required, current_user



views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", image_flie="website\static\logopowerlift.jpg", user=current_user)


@views.route('/cart')
def cart():
    return render_template("cart.html")

