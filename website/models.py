from __init__ import db
from flask_login import UserMixin
import requests
import json
import pprint

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True )
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    cart = db.relationship('Cart')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    cost = db.Column(db.Float)
    description = db.Column(db.String(275))
    cart = db.relationship('Cart')

    

    

    



class Cart(db.model):
    id = db.Column(db.Integer, primary_key="True")
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
    products_id = db.Column(db.Integer, db.ForeignKey("product.id"))