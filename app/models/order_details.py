from .db import db, environment, SCHEMA, add_prefix_for_prod

class OrderDetail(db.Model):
    __tablename__ = 'OrderDetails'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    order_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('Orders.id')), primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('Dishes.id')), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal_price = db.Column(db.Float, nullable=False)

    order = db.relationship("Order", back_populates="order_details")
    dish = db.relationship("Dish", back_populates="order_details", lazy=True)



    def to_dict(self):
        return {
            'order_id': self.order_id,
            'dish_id': self.dish_id,
            'quantity': self.quantity,
            'subtotal_price': self.subtotal_price
        }
