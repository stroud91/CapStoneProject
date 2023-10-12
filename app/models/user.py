from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    profile_image_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('userimages.id')))
    role = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)

    businesses_owned = db.relationship('Business', back_populates="owner")
    orders = db.relationship("Order", back_populates="user", lazy=True)
    reviews = db.relationship("Review", back_populates="user", lazy=True)
    profile_image = db.relationship("UserImage", back_populates="user")

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
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'profile_image_id': self.profile_image_id,
            'role': self.role,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'businesses': [business.to_dict() for business in self.businesses_owned]
        }
