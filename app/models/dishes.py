from .db import db, environment, SCHEMA, add_prefix_for_prod

class Dish(db.Model):
    __tablename__ = 'dishes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('business.id')))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    image_id = db.Column(db.String(length=1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('categories.id')))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)



    business = db.relationship("Business", back_populates="dishes")
    category = db.relationship("Category", back_populates="dishes")
    item = db.relationship('CartItem', back_populates='dish')
    order_details = db.relationship("OrderDetail", back_populates="dish", lazy=True, cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="dish", lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'name': self.name,
            'description': self.description,
            'image_id': self.image_id,
            'price': self.price,
            'category_id': self.category_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
