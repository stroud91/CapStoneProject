from .db import db, environment, SCHEMA, add_prefix_for_prod

class Dish(db.Model):
    __tablename__ = 'Dishes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    dish_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('Business.business_id')))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    image_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('Images.image_id')))
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('Categories.category_id')))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    business = db.relationship("Business", back_populates="dishes")
    category = db.relationship("Category", back_populates="dishes")
    image = db.relationship("Images", backref="dishes", lazy=True)
    order_details = db.relationship("OrderDetails", backref="dish", lazy=True)
    reviews = db.relationship("Reviews", backref="dish", lazy=True)

    def to_dict(self):
        return {
            'dish_id': self.dish_id,
            'business_id': self.business_id,
            'name': self.name,
            'description': self.description,
            'image_id': self.image_id,
            'price': self.price,
            'category_id': self.category_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
