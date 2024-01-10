from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    dish_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('dishes.id')))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=True)
    review_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", back_populates="reviews", lazy=True)
    dish = db.relationship("Dish", back_populates="reviews", lazy=True)


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'user_name': self.user.username,
            'dish_id': self.dish_id,
            'rating': self.rating,
            'comment': self.comment,
            'review_date': self.review_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'profile_image_id': self.user.profile_image_id
        }
