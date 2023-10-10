from .db import db, environment, SCHEMA

class OrderDetail(db.Model):
    __tablename__ = 'OrderDetails'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    order_id = db.Column(db.Integer, db.ForeignKey('Orders.order_id'), primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey('Dishes.dish_id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal_price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'dish_id': self.dish_id,
            'quantity': self.quantity,
            'subtotal_price': self.subtotal_price
        }
