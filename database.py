from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config


def create_database():
    app = Flask(__name__)
    app.config.from_object(Config)
    # my database
    db = SQLAlchemy(app)
    db.create_all()
    return app, db
