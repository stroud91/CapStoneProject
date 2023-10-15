from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from ..models import Order, db

order_bp = Blueprint('order', __name__)

@order_bp.route('/user/orders', methods=['GET'])
@login_required
def get_user_orders():
    try:
        orders = Order.query.filter_by(user_id=current_user.id).all()
        return jsonify([order.to_dict() for order in orders]), 200
    except Exception as e:
        return jsonify(error=str(e)), 400



@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
@login_required
def delete_order(order_id):
    try:

        order = Order.query.get_or_404(order_id)
        if order.user_id != current_user.id:
            return jsonify(error="Unauthorized"), 403


        db.session.delete(order)
        db.session.commit()

        return jsonify(message="Order deleted successfully"), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400
