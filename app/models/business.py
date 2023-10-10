
from .db import db, environment, SCHEMA

class Business(db.Model):
    __tablename__ = 'Business'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    business_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True, unique=True)
    logo_id = db.Column(db.Integer, db.ForeignKey('Images.image_id'))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'business_id': self.business_id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'logo_id': self.logo_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
