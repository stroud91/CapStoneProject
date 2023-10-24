from flask import Blueprint, request, jsonify
from datetime import datetime
from ..models import db, Cart, CartItem, Order, OrderDetail, Dish
from flask_login import login_required, current_user

cart_bp = Blueprint('cart', __name__)

# @cart_bp.route('/', methods=['GET'])
# @login_required
# def get_cart():
#     cart = Cart.query.filter_by(user_id=current_user.id).first()

#     if cart is None:
#         cart = Cart(
#             user_id=current_user.id,
#             created_at=datetime.utcnow(),
#             updated_at=datetime.utcnow()
#         )
#         db.session.add(cart)
#         db.session.commit()

#     return jsonify(cart.to_dict()), 200

# @cart_bp.route('/', methods=['POST'])
# @login_required
# def create_cart():
#     try:
#         new_cart = Cart(
#             user_id=current_user.id,
#             created_at=datetime.utcnow(),
#             updated_at=datetime.utcnow()
#         )
#         db.session.add(new_cart)
#         db.session.commit()
#         return jsonify(new_cart.to_dict()), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify(error=str(e)), 400

# @cart_bp.route('/<int:cart_id>/items', methods=['POST'])
# @login_required
# def add_item_to_cart(cart_id):
#     data = request.get_json()
#     try:
#         new_item = CartItem(
#             cart_id=cart_id,
#             dish_id=data['dish_id'],
#             quantity=data['quantity'],
#             created_at=datetime.utcnow(),
#             updated_at=datetime.utcnow()
#         )
#         db.session.add(new_item)
#         db.session.commit()
#         return jsonify(new_item.to_dict()), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify(error=str(e)), 400

@cart_bp.route('/', methods=['GET', 'POST'])
@login_required
def handle_cart():
    if request.method == 'GET':
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        if cart is None:
            cart = Cart(user_id=current_user.id, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
            db.session.add(cart)
            db.session.commit()
        return jsonify(cart.to_dict()), 200
    else:
        # Handle POST logic for explicit cart creation
        data = request.get_json()  # Get data sent with the request
        # You can use the data for some initial settings if needed
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        if cart:
            return jsonify(error="Cart already exists for this user"), 400
        new_cart = Cart(user_id=current_user.id, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add(new_cart)
        try:
            db.session.commit()
            return jsonify(new_cart.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify(error=str(e)), 400


@cart_bp.route('/<int:cart_id>/items', methods=['POST'])
@login_required
def add_item_to_cart(cart_id):
    data = request.get_json()
    existing_item = CartItem.query.filter_by(cart_id=cart_id, dish_id=data['dish_id']).first()

    if existing_item:
        existing_item.quantity += data['quantity']
    else:
        new_item = CartItem(cart_id=cart_id, dish_id=data['dish_id'], quantity=data['quantity'], created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add(new_item)

    try:
        db.session.commit()
        return jsonify(new_item.to_dict() if not existing_item else existing_item.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400

@cart_bp.route('/<int:cart_id>/items/<int:item_id>', methods=['DELETE'])
@login_required
def delete_item_from_cart(cart_id, item_id):
    item = CartItem.query.get(item_id)
    if not item:
        return jsonify(error="Item not found"), 404

    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify(message="Item removed successfully"), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400


@cart_bp.route('/submit_cart', methods=['POST'])
@login_required
def submit_cart():
    try:
        # Fetch current user's cart
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        if not cart:
            return jsonify(error="No active cart for the user"), 400

        # Create new order
        new_order = Order(
            user_id=current_user.id,
            total_price=0,  # we'll update this later
            order_date=datetime.utcnow(),
            delivery_address=request.json.get('delivery_address'),
            status="Pending",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_order)

        # Process cart items and add them to order details
        total_price = 0
        cart_items_to_delete = []
        for item in cart.items:
            dish = Dish.query.get(item.dish_id)
            if not dish:
                raise Exception("Dish not found")

            subtotal = dish.price * item.quantity
            order_detail = OrderDetail(
                order_id=new_order.id,
                dish_id=item.dish_id,
                quantity=item.quantity,
                subtotal_price=subtotal
            )
            total_price += subtotal
            db.session.add(order_detail)
            cart_items_to_delete.append(item)  # Add item to delete list

        # Update order total price
        new_order.total_price = total_price

        # Delete cart items and the cart itself
        for item in cart_items_to_delete:
            db.session.delete(item)
        db.session.delete(cart)

        db.session.commit()  # Commit the transaction

        return jsonify(message="Order submitted successfully", order=new_order.to_dict()), 201
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of errors
        return jsonify(error=str(e)), 400

