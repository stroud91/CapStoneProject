
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Business(db.Model):
    __tablename__ = 'business'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String(length=50), nullable=False)
    state = db.Column(db.String(length=25), nullable=False)
    zip_code = db.Column(db.String(length=10), nullable=False)
    about = db.Column(db.String(length=500), nullable=False)
    phone_number = db.Column(db.String(length=30), nullable=False)
    type = db.Column(db.String(length=255), nullable=False)
    email = db.Column(db.String, nullable=True, unique=True)
    logo_id = db.Column(db.String(length=1000), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    owner = db.relationship("User", back_populates="businesses_owned")
    dishes = db.relationship("Dish", back_populates="business", lazy=True)



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'phone': self.phone_number,
            'about': self.about,
            'type': self.type,
            'email': self.email,
            'logo_id': self.logo_id,
            'owner_id': self.owner_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
