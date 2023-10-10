
from .db import db, environment, SCHEMA

class Category(db.Model):
    __tablename__ = 'Categories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

    dishes = db.relationship("Dish", back_populates="category", lazy=True)

    def to_dict(self):
        return {
            'category_id': self.category_id,
            'name': self.name,
            'description': self.description
        }
