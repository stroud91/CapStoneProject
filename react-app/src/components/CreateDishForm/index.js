

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

  const [formData, setFormData] = useState({
    name: "",
    description: "",
    price: "",
    image_id: "",
    category_id: CATEGORIES[0].id,

  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

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
    <div className="dish-form-container">
      <form onSubmit={handleSubmit}>

        {/* Name Field */}
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
        </div>

        {/* Description Field */}
        <div className="form-group">
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleInputChange}
          ></textarea>
        </div>

        {/* Price Field */}
        <div className="form-group">
          <label htmlFor="price">Price:</label>
          <input
            type="number"
            id="price"
            name="price"
            value={formData.price}
            onChange={handleInputChange}
            required
          />
        </div>

        {/* Image ID  */}
        <div className="form-group">
          <label htmlFor="image_id">Image ID:</label>
          <input
            type="text"
            id="image_id"
            name="image_id"
            value={formData.image_id}
            onChange={handleInputChange}
          />
        </div>

        {/* Category Dropdown */}
        <div className="form-group">
          <label htmlFor="category">Category:</label>
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
        </div>

        {/* Submit Button */}
        <div className="form-group">
          <button type="submit">Add Dish</button>
        </div>
      </form>
    </div>
  );
}

export default DishCreationForm;
