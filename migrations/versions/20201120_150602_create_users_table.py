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
    op.create_table(
        'Images',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('image_url', sa.String, unique=True, nullable=False),
        sa.Column('alt_text', sa.String, nullable=True),
        sa.Column('image_type', sa.String, nullable=False),
        sa.Column('preview', sa.Boolean, nullable=False, default=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('uploaded_at', sa.DateTime, nullable=False)
    )

    # Creating the Users table
    op.create_table(
        'Users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String, nullable=False, unique=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('first_name', sa.String, nullable=True),
        sa.Column('last_name', sa.String, nullable=True),
        sa.Column('password_hash', sa.String, nullable=False),
        sa.Column('address', sa.String, nullable=True),
        sa.Column('phone', sa.String, nullable=True),
        sa.Column('profile_image_id', sa.Integer, sa.ForeignKey('Images.id')),
        sa.Column('role', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")

     # Creating the Business table
    op.create_table(
        'Business',
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
        sa.Column('logo_id', sa.Integer, sa.ForeignKey('Images.id')),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('Users.id')),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

    # Creating the Categories table
    op.create_table(
        'Categories',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True)
    )

    # Creating the Dishes table
    op.create_table(
        'Dishes',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('business_id', sa.Integer, sa.ForeignKey('Business.id')),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('image_id', sa.Integer, sa.ForeignKey('Images.id')),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('Categories.id')),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

    # Creating the Orders table
    op.create_table(
        'Orders',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('Users.id')),
        sa.Column('total_price', sa.Float, nullable=False),
        sa.Column('order_date', sa.DateTime, nullable=False),
        sa.Column('delivery_address', sa.String, nullable=False),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

    # Creating the OrderDetails table
    op.create_table(
        'OrderDetails',
        sa.Column('order_id', sa.Integer, sa.ForeignKey('Orders.id')),
        sa.Column('dish_id', sa.Integer, sa.ForeignKey('Dishes.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('subtotal_price', sa.Float, nullable=False),
        sa.PrimaryKeyConstraint('order_id', 'dish_id')
    )

    # Creating the Reviews table
    op.create_table(
        'Reviews',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('Users.id')),
        sa.Column('dish_id', sa.Integer, sa.ForeignKey('Dishes.id')),
        sa.Column('rating', sa.Integer, nullable=False),
        sa.Column('comment', sa.String, nullable=True),
        sa.Column('review_date', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )

def downgrade():
    op.drop_table('Reviews')
    op.drop_table('OrderDetails')
    op.drop_table('Orders')
    op.drop_table('Dishes')
    op.drop_table('Categories')
    op.drop_table('Business')
    op.drop_table('Users')
    op.drop_table('Images')
