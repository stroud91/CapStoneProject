# images.py

from .db import db, environment, SCHEMA

class Image(db.Model):
    __tablename__ = 'images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_url = db.Column(db.String, unique=True, nullable=False)
    alt_text = db.Column(db.String, nullable=True)
    image_type = db.Column(db.String, nullable=False)
    preview = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", back_populates="profile_image", uselist=False)
    business = db.relationship("Business", back_populates="logo", uselist=False)
    dishes = db.relationship("Dish", back_populates="image", lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'alt_text': self.alt_text,
            'image_type': self.image_type,
            'preview': self.preview,
            'created_at': self.created_at,
            'uploaded_at': self.uploaded_at
        }
