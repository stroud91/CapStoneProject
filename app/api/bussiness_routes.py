from flask import Blueprint, request, jsonify
from ..models import db, Business, Review, Dish
from ..forms.bussiness import BusinessForm
from flask_login import login_required, current_user
from datetime import datetime
from werkzeug.utils import secure_filename
from sqlalchemy.exc import SQLAlchemyError
import os

business_bp = Blueprint('business', __name__)


#get all bussiness
@business_bp.route('/', methods=['GET'])
def get_all_businesses():
    businesses = Business.query.all()
    businesses_data = [business.to_dict() for business in businesses]
    return jsonify(businesses_data)


#get one bussiness
@business_bp.route('/<int:business_id>', methods=['GET'])
def get_single_business(business_id):
    business = Business.query.get_or_404(business_id)
    business_data = business.to_dict()

    dishes_data = []
    for dish in business.dishes:
        dish_data = dish.to_dict()
        
        reviews_data = []
        for review in dish.reviews:
            review_data = review.to_dict()
            reviews_data.append(review_data)

        dish_data['reviews'] = reviews_data
        dishes_data.append(dish_data)

    business_data['dishes'] = dishes_data
    return jsonify(business_data)


@business_bp.route('/new-business', methods=['POST'])
@login_required
def add_business():
    form = BusinessForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        business = Business(
            name=form.name.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data,
            zip_code=form.zip_code.data,
            phone_number=form.phone_number.data,
            about=form.about.data,
            type=form.type.data,
            email=form.email.data,
            logo_url=form.logo_url.data,
            owner_id=form.owner_id.data,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        db.session.add(business)
        db.session.commit()

        return jsonify(business.to_dict())
    else:
        return jsonify({"errors": form.errors}), 400





#update a bussiness
@business_bp.route('/<int:b_id>/edit', methods=['POST'])
@login_required
def edit_business(b_id):
    form = BusinessForm()
    business = Business.query.get(b_id)

    if not business:
        return jsonify({"error": "Business not found"}), 404

    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to edit this business"}), 403

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        attributes_to_update = [
            'name', 'address', 'city', 'state',
            'zip_code', 'phone_number', 'category_id',
            'website', 'about', 'type', 'logo_url'
        ]
        for attr in attributes_to_update:
            if hasattr(form, attr):
                setattr(business, attr, getattr(form, attr).data)

        business.updated_at = datetime.utcnow()
        db.session.commit()

        return jsonify(business.to_dict())
    else:
        return {"errors": form.errors}


#delete a bussiness
@business_bp.route('/<int:b_id>/delete', methods=['DELETE'])
@login_required
def delete_business(b_id):
    business = Business.query.get(b_id)

    if not business:
        return jsonify({"error": "Business not found"}), 404

    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to delete this business"}), 403

    temp = business.to_dict()

    try:

        for dish in business.dishes:
            for review in dish.reviews:
                db.session.delete(review)

            db.session.delete(dish)


        db.session.delete(business)
        db.session.commit()

        response = {
            "message": "Business successfully deleted.",
        }

        return jsonify(response)

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while deleting the business", "message": str(e)}), 500
