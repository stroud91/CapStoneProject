from flask import render_template, redirect, url_for, request, flash , Blueprint, jsonify
from ..forms.dishes import DishForm
from ..models import Dish , db
from flask import request
from datetime import datetime


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





@dish_bp.route('/add', methods=['GET', 'POST'])
def add_dish():
    form = DishForm()

    if form.validate_on_submit():
        new_dish = Dish(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            image_id='',
            category_id=form.category_id.data,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        db.session.add(new_dish)
        db.session.commit()



        return redirect(url_for('dish.get_all_dishes'))

    return render_template('add_dish.html', form=form)



@dish_bp.route('/update/<int:dish_id>', methods=['GET', 'POST'])
def update_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    form = DishForm(obj=dish)

    if request.method == 'POST' and form.validate():
        dish.name = form.name.data
        dish.description = form.description.data
        dish.price = form.price.data
        dish.category_id = form.category_id.data
        dish.updated_at = datetime.utcnow()

        

        db.session.commit()
        flash('Dish updated successfully!', 'success')
        return redirect(url_for('dish_bp.get_dish', dish_id=dish.id))

    return render_template('update_dish.html', form=form, dish=dish)



@dish_bp.route('/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)

    db.session.delete(dish)
    db.session.commit()

    return jsonify({"message": "Dish deleted"}), 204
