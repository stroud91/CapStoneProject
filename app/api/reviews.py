from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models import Review, db,Dish
from ..forms.reviews import ReviewForm
from datetime import datetime
review_routes = Blueprint('reviews', __name__)

@review_routes.route('/', methods=['GET'])
def get_all_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])

@review_routes.route('/business/<int:business_id>', methods=['GET'])
def get_reviews_for_business(business_id):

    dishes = Dish.query.filter_by(business_id=business_id).all()


    dish_ids = [dish.id for dish in dishes]


    reviews = Review.query.filter(Review.dish_id.in_(dish_ids)).all()

    return jsonify([review.to_dict() for review in reviews])


@review_routes.route('/dish/<int:dish_id>', methods=['GET'])
def get_reviews_for_dish(dish_id):
    reviews = Review.query.filter_by(dish_id=dish_id).all()
    return jsonify([review.to_dict() for review in reviews])

@review_routes.route('/user', methods=['GET'])
@login_required
def get_user_reviews():
    reviews = Review.query.filter_by(user_id=current_user.id).all()
    return jsonify([review.to_dict() for review in reviews])

@review_routes.route('/<int:review_id>', methods=['GET'])
def get_single_review(review_id):
    review = Review.query.get_or_404(review_id)
    return jsonify(review.to_dict())

@review_routes.route('/create', methods=['POST'])
@login_required
def create_review():
    form = ReviewForm()
    form_data = request.get_json()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_review = Review(
            comment=form_data['comment'],
            rating=form_data['rating'],
            user_id=current_user.id,
            dish_id=form_data['dish_id'],
            review_date=datetime.utcnow(),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()

        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201

    return jsonify(form.errors), 400

@review_routes.route('/<int:review_id>', methods=['PUT'])
@login_required

def update_review(review_id):
    review = Review.query.get_or_404(review_id)
    if review.user_id != current_user.id:
        return jsonify(error="Not authorized"), 403

    form = ReviewForm()
    form_data = request.get_json()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review.comment = form_data['comment']
        review.rating = form_data['rating']
        db.session.commit()
        return jsonify(review.to_dict()), 200

    return jsonify(form.errors), 400

@review_routes.route('/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    
    if review.user_id != current_user.id:
        return jsonify(error="Not authorized"), 403

    db.session.delete(review)
    db.session.commit()
    return jsonify(message="Review deleted"), 200
