# reviews.py

from .db import db, environment, SCHEMA

class Review(db.Model):
    __tablename__ = 'Reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    dish_id = db.Column(db.Integer, db.ForeignKey('Dishes.dish_id'))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=True)
    review_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'dish_id': self.dish_id,
            'rating': self.rating,
            'comment': self.comment,
            'review_date': self.review_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
