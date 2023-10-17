from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from ..models import OrderDetail, Dish, Business, Order, User, db
from datetime import datetime
owner_bp = Blueprint('owner', __name__)

@owner_bp.route('/business/<int:business_id>/orders', methods=['GET'])
@login_required
def get_business_orders(business_id):
    try:
        
        business = Business.query.get_or_404(business_id)
        if business.owner_id != current_user.id:
            return jsonify(error="Unauthorized"), 403


        orders = (
            Order.query
            .join(OrderDetail)
            .join(Dish)
            .filter(Dish.business_id == business_id)
            .distinct(Order.id)
            .all()
        )
        return jsonify([order.to_dict() for order in orders]), 200
    except Exception as e:
        return jsonify(error=str(e)), 400


@owner_bp.route('/<int:order_id>/status', methods=['PATCH'])
@login_required
def update_order_status(order_id):
    """
    Update order status.
    - Only the business owner can update it.
    - Expected JSON: {"status": "new_status"}
    """
    try:
        order = Order.query.get_or_404(order_id)


        # if current_user.role != 'owner' or not user_owns_order_business(current_user, order):
        #     return jsonify(error="Unauthorized"), 403

        data = request.get_json()
        order.status = data['status']
        order.updated_at = datetime.utcnow()

        db.session.commit()
        return jsonify(order.to_dict()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400


@owner_bp.route('/<int:order_id>', methods=['DELETE'])
@login_required
def delete_order_by_owner(order_id):
    """
    Delete an order.
    - Only the business owner can delete it.
    """
    try:
        order = Order.query.get_or_404(order_id)

        # if current_user.role != 'owner' or not user_owns_order_business(current_user, order):
        #     return jsonify(error="Unauthorized"), 403

        db.session.delete(order)
        db.session.commit()
        return jsonify(message="Order deleted successfully"), 200

    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400
