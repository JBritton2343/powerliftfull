from . import db
from flask_login import UserMixin

class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True )
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    cart = db.relationship('Cart')

class Products(db.model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.string(200))
    cost = db.Column(db.Float)
    description = db.Column(db.String(275))
    cart = db.relationship('Cart')


class Cart(db.model):
    id = db.Column(db.Integer, primary_key="True")
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
    products_id = db.Column(db.Integer, db.ForeignKey("product.id"))