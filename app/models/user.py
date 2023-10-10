from .db import db, environment, SCHEMA
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    profile_image_id = db.Column(db.Integer, db.ForeignKey('Images.image_id'))
    role = db.Column(db.String, nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('Business.business_id'))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'profile_image_id': self.profile_image_id,
            'role': self.role,
            'business_id': self.business_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
