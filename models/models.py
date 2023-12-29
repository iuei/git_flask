# models/models.py
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class user_list(db.Model, UserMixin):
    __tablename__ = 'user_list'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cell = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.String(255))
    address = db.Column(db.String(255))

    def check_password(self, password):
        return check_password_hash(self.password, password)


class commodity(db.Model, UserMixin):
    __tablename__ = 'commodity'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.String(10))
    type = db.Column(db.String(100))