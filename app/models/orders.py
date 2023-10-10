from .db import db, environment, SCHEMA

class Order(db.Model):
    __tablename__ = 'Orders'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    delivery_address = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'total_price': self.total_price,
            'order_date': self.order_date,
            'delivery_address': self.delivery_address,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
