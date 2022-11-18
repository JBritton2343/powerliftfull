from . import db
from flask_login import UserMixin
import requests
import json
import pprint

class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True )
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    cart = db.relationship('Cart')

class Products(db.model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.string(200))
    cost = db.Column(db.Float)
    description = db.Column(db.String(275))
    cart = db.relationship('Cart')

    url="https://comppartsapi.herokuapp/computerparts"
    params = {"part": "cases", "part":"cpucoolers","part":"motherboard", "part":"cpu", "part":"videocard", "part":"memory", "part":"storage", "part":"powersupply", "part":"cases" }
    response = requests.get(url, params)

    if response.status_code == 200:
        response_dict=response.json()
        for items in response_dict:
            requests.post(Products)
            
    else:
        print(f"error: {response.status_code}")

    



class Cart(db.model):
    id = db.Column(db.Integer, primary_key="True")
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
    products_id = db.Column(db.Integer, db.ForeignKey("product.id"))