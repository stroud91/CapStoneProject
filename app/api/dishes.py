from flask import render_template, redirect, url_for, request, flash , Blueprint, jsonify
from ..forms.dishes import DishForm
from ..models import Business, Dish, db, Review, OrderDetail
from flask import request
from datetime import datetime
from flask_login import login_required, current_user
from sqlalchemy.sql import func

dish_bp = Blueprint('dish', __name__)

@dish_bp.route('/', methods=['GET'])
def get_all_dishes():
    dishes = Dish.query.all()
    dishes_data = [dish.to_dict() for dish in dishes]
    return jsonify(dishes_data)


@dish_bp.route('/business/<int:business_id>', methods=['GET'])
def get_all_dishes_for_business(business_id):
    dishes = Dish.query.filter_by(business_id=business_id).all()
    dishes_data = [dish.to_dict() for dish in dishes]
    return jsonify(dishes_data)



@dish_bp.route('/<int:dish_id>', methods=['GET'])
def get_single_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    return jsonify(dish.to_dict())





@dish_bp.route('/business/<int:business_id>/add', methods=['POST'])
@login_required
def add_dish(business_id):
    business = Business.query.get_or_404(business_id)


    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to add a dish for this business"}), 403


    form = DishForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate():
        new_dish = Dish(
            business_id=business_id,
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            image_id=request.json.get('image_id', ''),
            category_id=form.category_id.data,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        db.session.add(new_dish)
        db.session.commit()

        return jsonify(new_dish.to_dict()), 201


    return jsonify({"error": form.errors}), 400





@dish_bp.route('/business/<int:business_id>/update/<int:dish_id>', methods=['GET', 'POST'])
@login_required
def update_dish(business_id, dish_id):
    dish = Dish.query.get_or_404(dish_id)
    business = Business.query.get_or_404(business_id)


    if dish.business_id != business.id:
        return jsonify({"error": "Dish does not belong to this business"}), 403


    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to update this dish"}), 403

    form = DishForm(obj=dish)
    form['csrf_token'].data = request.cookies['csrf_token']
    if request.method == 'POST' and form.validate():
        dish.name = form.name.data
        dish.description = form.description.data
        dish.price = form.price.data
        dish.category_id = form.category_id.data
        dish.updated_at = datetime.utcnow()

        db.session.commit()

        return jsonify(dish.to_dict()), 200


    return jsonify({"error": "Validation failed or GET request"}), 400





@dish_bp.route('/business/<int:business_id>/dish/<int:dish_id>', methods=['DELETE'])
@login_required
def delete_dish(business_id, dish_id):

    dish = Dish.query.get_or_404(dish_id)
    business = Business.query.get_or_404(business_id)


    if dish.business_id != business.id:
        return jsonify({"error": "Dish does not belong to the provided business"}), 400


    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to delete this dish"}), 403

    db.session.delete(dish)
    db.session.commit()

    return jsonify({"message": "Dish and its reviews deleted"}), 204

# Top Rated Dishes route
@dish_bp.route('/top-rated', methods=['GET'])
def get_top_rated_dishes():
    top_rated_dishes = db.session.query(Dish, func.avg(Review.rating).label('average_rating'))\
        .join(Review, Dish.id == Review.dish_id)\
        .group_by(Dish.id)\
        .order_by(func.avg(Review.rating).desc())\
        .limit(3).all()

    dishes_data = [{'id': dish.id, 'name': dish.name, 'rating': average_rating, 'image_id': dish.image_id} for dish, average_rating in top_rated_dishes]
    return jsonify(dishes_data)


# Top Ordered Dishes route
@dish_bp.route('/top-ordered', methods=['GET'])
def get_top_ordered_dishes():
    top_ordered_dishes = db.session.query(Dish, func.count(OrderDetail.dish_id).label('order_count'))\
        .join(OrderDetail, Dish.id == OrderDetail.dish_id)\
        .group_by(Dish.id)\
        .order_by(func.count(OrderDetail.dish_id).desc())\
        .limit(3).all()

    dishes_data = [{'id': dish.id, 'name': dish.name, 'orders': order_count, 'image_id': dish.image_id} for dish, order_count in top_ordered_dishes]
    return jsonify(dishes_data)
