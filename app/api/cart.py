from flask import Blueprint, request, jsonify
from datetime import datetime
from ..models import db, Cart, CartItem, Order, OrderDetail, Dish
from flask_login import login_required, current_user

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/', methods=['GET'])
@login_required
def get_cart():
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    if cart is None:
        cart = Cart(
            user_id=current_user.id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(cart)
        db.session.commit()

    return jsonify(cart.to_dict()), 200

@cart_bp.route('/', methods=['POST'])
@login_required
def create_cart():
    try:
        new_cart = Cart(
            user_id=current_user.id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_cart)
        db.session.commit()
        return jsonify(new_cart.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400

@cart_bp.route('/<int:cart_id>/items', methods=['POST'])
@login_required
def add_item_to_cart(cart_id):
    data = request.get_json()
    try:
        new_item = CartItem(
            cart_id=cart_id,
            dish_id=data['dish_id'],
            quantity=data['quantity'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400

@cart_bp.route('/<int:cart_id>/submit', methods=['POST'])
@login_required
def submit_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    data = request.get_json()
    try:
        new_order = Order(
            user_id=current_user.id,
            total_price=data['total_price'],
            order_date=datetime.utcnow(),
            delivery_address=data['delivery_address'],
            status="Submitted",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_order)
        db.session.flush()

        for item in cart.items:
            dish = Dish.query.get_or_404(item.dish_id)
            order_detail = OrderDetail(
                order_id=new_order.id,
                dish_id=item.dish_id,
                quantity=item.quantity,
                subtotal_price=item.quantity * dish.price
            )
            db.session.add(order_detail)

        db.session.delete(cart)
        db.session.commit()

        return jsonify(new_order.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400
