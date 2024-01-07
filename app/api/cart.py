from flask import Blueprint, request, jsonify
from datetime import datetime
from ..models import db, Cart, CartItem, Order, OrderDetail, Dish
from flask_login import login_required, current_user

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/view', methods=['GET'])
def view_cart():

    user_id = current_user.id


    cart = Cart.query.filter_by(user_id=user_id).first()

    if not cart:
        return jsonify({'error': 'No cart found for the user'}), 404


    cart_data = {
        'cart_id': cart.id,
        'created_at': cart.created_at,
        'updated_at': cart.updated_at,
        'items': []
    }

    for item in cart.items:
        cart_item_data = {
            'item_id': item.id,
            'dish_id': item.dish_id,
            'quantity': item.quantity,
            'created_at': item.created_at,
            'updated_at': item.updated_at
        }

        cart_data['items'].append(cart_item_data)

    return jsonify(cart_data), 200


@cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    dish_id = request.json['dish_id']
    quantity = request.json['quantity']


    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        cart = Cart(user_id=current_user.id, created_at=datetime.now(), updated_at=datetime.now())
        db.session.add(cart)
        db.session.commit()


    cart_item = CartItem.query.filter_by(cart_id=cart.id, dish_id=dish_id).first()


    if cart_item:
        cart_item.quantity += quantity
        db.session.commit()
        return jsonify(cart_item.to_dict()), 200
    else:

        new_cart_item = CartItem(
            cart_id=cart.id,
            dish_id=dish_id,
            quantity=quantity,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(new_cart_item)
        db.session.commit()
        return jsonify(new_cart_item.to_dict()), 201




@cart_bp.route('/update', methods=['POST'])
def update_cart():
    cart_item_id = request.json['cart_item_id']
    change = request.json['change']

    cart_item = CartItem.query.get(cart_item_id)
    if cart_item:

        cart_item.quantity = max(1, cart_item.quantity + change)
        db.session.commit()

        return jsonify(cart_item.to_dict()), 200
    else:
        return jsonify({'error': 'Cart item not found'}), 404


@cart_bp.route('/remove', methods=['POST'])
def remove_from_cart():

    cart_item_id = request.json['cart_item_id']

    cart_item = CartItem.query.get(cart_item_id)
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'message': 'Item removed from cart'}), 200
    else:
        return jsonify({'error': 'Cart item not found'}), 404


@cart_bp.route('/submit', methods=['POST'])
@login_required
def submit_cart():
    user_id = current_user.id
    cart = Cart.query.filter_by(user_id=user_id).first()

    if cart:

        CartItem.query.filter_by(cart_id=cart.id).delete()
        db.session.commit()

        return jsonify({'message': 'Cart submitted and emptied'}), 200
    else:
        return jsonify({'error': 'Cart not found'}), 404
