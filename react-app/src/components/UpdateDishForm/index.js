import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import { editDishForBusiness } from '../../store/dish';
import './UpdateDishForm.css';
import { setSingleDish } from '../../store/dish';
import { setDishesForBusiness } from '../../store/dish';



function DishUpdateForm() {
  const dispatch = useDispatch();
  const history = useHistory();
  const {businessId, id} = useParams();
  console.log("this is use params for bid and id", businessId, id)
  const currentDish = useSelector(state =>
    state.dish.list
      ? state.dish.list.find(dish => dish.id === parseInt(id))
      : null
  );
  console.log("this is current dish for update form", currentDish)
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

  const [formData, setFormData] = useState({
    id: currentDish ? currentDish.id : null,
    business_id: currentDish ? currentDish.business_id : null,
    name: currentDish ? currentDish.name : '',
    description: currentDish ? currentDish.description : '',
    price: currentDish ? currentDish.price : '',
    category_id: currentDish ? currentDish.category_id : null,
    image_id: currentDish ? currentDish.image_id : null,
  });


  useEffect(() => {
       setSingleDish(id)
       setDishesForBusiness(id)
  }, [dispatch, id]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch(editDishForBusiness(businessId, id, formData))
      .then(() => {
        alert('Dish updated successfully!');
        history.push(`/business/${businessId}`);
      })
      .catch(() => {
        console.error("Failed to update dish");
        alert('Failed to update dish. Please try again.');
      });
  };

  return (
    <div className="update-dish-form-container">
      <h2>Update Dish</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label>Description:</label>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label>Price:</label>
          <input
            type="number"
            name="price"
            value={formData.price}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label>Category:</label>
          <select
            name="category_id"
            value={formData.category_id}
            onChange={handleInputChange}
            required
          >
            {CATEGORIES.map(category => (
              <option key={category.id} value={category.id}>
                {category.name}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label>Image:</label>
          <input
            type="text"
            name="image_id"
            value={formData.image_id}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <button type="submit">Update Dish</button>
        </div>
      </form>
    </div>
  );
}

export default DishUpdateForm;
