from os import path
from flask import Flask

from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'absitante834nf09892nf9'
    app.config["SQLALCHEMY.DATABASE.URI"] = f'SQLITE:///{DB_NAME}'
    db.init.app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prifix='/')

    from .models import User, Products, Cart

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Database Created!")    
