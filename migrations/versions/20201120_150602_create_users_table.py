"""create_users_table

Revision ID: ffdc0a98111c
Revises:
Create Date: 2020-11-20 15:06:02.230689

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'ffdc0a98111c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Creating the Images table

    # Creating the Users table
    op.create_table('userimages',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('image_url', sa.String, unique=True, nullable=False),
        sa.Column('alt_text', sa.String, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('uploaded_at', sa.DateTime, nullable=False),
    )

    op.create_table('businessimages',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('image_url', sa.String, unique=True, nullable=False),
        sa.Column('alt_text', sa.String, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('uploaded_at', sa.DateTime, nullable=False),
    )

    op.create_table('dishimages',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('image_url', sa.String, unique=True, nullable=False),
        sa.Column('alt_text', sa.String, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('uploaded_at', sa.DateTime, nullable=False),
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String, nullable=False, unique=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('first_name', sa.String, nullable=True),
        sa.Column('last_name', sa.String, nullable=True),
        sa.Column('password_hash', sa.String, nullable=False),
        sa.Column('address', sa.String, nullable=True),
        sa.Column('phone', sa.String, nullable=True),
        sa.Column('profile_image_id', sa.Integer, sa.ForeignKey('userimages.id')),
        sa.Column('role', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

     # Creating the Business table
    op.create_table(
        'business',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('address', sa.String, nullable=False),
        sa.Column('city', sa.String(length=50), nullable=False),
        sa.Column('state', sa.String(length=25), nullable=False),
        sa.Column('zip_code', sa.String(length=10), nullable=False),
        sa.Column('about', sa.String(length=500), nullable=False),
        sa.Column('phone_number', sa.String(length=30), nullable=False),
        sa.Column('type', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String, nullable=True, unique=True),
        sa.Column('logo_id', sa.Integer, sa.ForeignKey('businessimages.id')),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

    # Creating the Categories table
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True)
    )

    # Creating the Dishes table
    op.create_table(
        'dishes',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('business_id', sa.Integer, sa.ForeignKey('business.id')),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('image_id', sa.Integer, sa.ForeignKey('dishimages.id')),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id')),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

    # Creating the Orders table
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('total_price', sa.Float, nullable=False),
        sa.Column('order_date', sa.DateTime, nullable=False),
        sa.Column('delivery_address', sa.String, nullable=False),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

    # Creating the OrderDetails table
    op.create_table(
        'orderdetails',
        sa.Column('order_id', sa.Integer, sa.ForeignKey('orders.id')),
        sa.Column('dish_id', sa.Integer, sa.ForeignKey('dishes.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('subtotal_price', sa.Float, nullable=False),
        sa.PrimaryKeyConstraint('order_id', 'dish_id')
    )

    # Creating the Reviews table
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('dish_id', sa.Integer, sa.ForeignKey('dishes.id')),
        sa.Column('rating', sa.Integer, nullable=False),
        sa.Column('comment', sa.String, nullable=True),
        sa.Column('review_date', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

    if environment == "production":
      op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")


def downgrade():
    op.drop_table('reviews')
    op.drop_table('orderdetails')
    op.drop_table('orders')
    op.drop_table('dishes')
    op.drop_table('categories')
    op.drop_table('business')
    op.drop_table('users')
    op.drop_table('userimages')
    op.drop_table('businessimages')
    op.drop_table('dishimages')
