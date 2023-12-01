

import React, { useState } from 'react';
import { useDispatch,useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';

import { createDishForBusiness } from '../../store/dish';

const CATEGORIES = [
  { id: 1, name: 'Asian' },
  { id: 2, name: 'European' },
  { id: 3, name: 'Vegetarian' },
  { id: 4, name: 'Vegan' },
  { id: 5, name: 'Gluten-Free' },
  { id: 6, name: 'Seafood' },
  { id: 7, name: 'Fast Food' },
  { id: 8, name: 'Bakery' },
  { id: 9, name: 'Dessert' },
  { id: 10, name: 'Drinks' },
  { id: 11, name: 'Breakfast' },
  { id: 12, name: 'Snacks' },
  { id: 13, name: 'Barbecue' },
  { id: 14, name: 'Salads' },
  { id: 15, name: 'Soups' }
];

function DishCreationForm() {

 const dispatch = useDispatch();
 const history = useHistory();
 const selectedBusiness = useSelector(state => state.business.selectedBusiness);
 const [validationErrors, setValidationErrors] = useState([]);

  const [formData, setFormData] = useState({
    name: "",
    description: "",
    price: "",
    image_id: "",
    category_id: CATEGORIES[0].id,

  });

  const validate = () => {
    const errors = {};

    if (!formData.name) {
      errors.name = "Dish name is required.";
    }

    if (formData.description.length > 500) {
      errors.description = "Description should be under 500 characters.";
    }

    if (formData.price <= 0) {
      errors.price = "Price should be a positive value.";
    }

    if (!formData.image_id) {
      errors.image_id = "Image ID is required.";
    }
    return errors;
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const errors = validate();

    if (Object.keys(errors).length > 0) {
      setValidationErrors(errors);
      return;
  }

    const dishData = {
      name: formData.name,
      description: formData.description,
      price: formData.price,
      image_id: formData.image_id,
      category_id: formData.category_id,
    };

    await dispatch(createDishForBusiness(selectedBusiness.id, dishData));

    history.push(`/business/${selectedBusiness.id}`);
  };

  return (

    <div className="business-form-container">
      <h3 className="dish-form-heading">Create Your Menu Item</h3>
      <form onSubmit={handleSubmit} className="form-group">

        {/* Name Field */}

          <label htmlFor="name">Name:
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}

          />
          {validationErrors.name && <div className="error">{validationErrors.name}</div>}
          </label>

        {/* Description Field */}

          <label htmlFor="description">Description:
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleInputChange}
          ></textarea>
          {validationErrors.description && <div className="error">{validationErrors.description}</div>}
          </label>

        {/* Price Field */}

          <label htmlFor="price">Price:
          <input
            type="number"
            id="price"
            name="price"
            value={formData.price}
            onChange={handleInputChange}

          />
          {validationErrors.price && <div className="error">{validationErrors.price}</div>}
          </label>

        {/* Image ID  */}

          <label htmlFor="image_id">Image ID:
          <input
            type="text"
            id="image_id"
            name="image_id"
            value={formData.image_id}
            onChange={handleInputChange}
          />
          {validationErrors.image_id && <div className="error">{validationErrors.image_id}</div>}
          </label>

        {/* Category Dropdown */}

          <label htmlFor="category">Category:
          <select
            id="category"
            name="category_id"
            value={formData.category_id}
            onChange={handleInputChange}
          >
            {CATEGORIES.map(category => (
              <option key={category.id} value={category.id}>
                {category.name}
              </option>
            ))}
          </select>
          </label>

        {/* Submit Button */}

          <button type="submit">Add Dish</button>

      </form>
    </div>

  );
}

export default DishCreationForm;
