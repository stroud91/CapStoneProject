from app.models import db, UserImage, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_user_images():
    base_url = "https://robohash.org/"
    images = []

    for i in range(1, 101):
        image_url = base_url + str(i)
        new_image = UserImage(
            image_url=image_url,
            alt_text=f"Profile image for user_{i}",
            created_at=datetime.datetime.now(),
            uploaded_at=datetime.datetime.now()
        )
        images.append(new_image)

    db.session.add_all(images)
    db.session.commit()

def undo_user_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.userimages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM userimages"))

    db.session.commit()
