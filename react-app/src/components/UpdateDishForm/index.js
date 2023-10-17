import React, { useState } from 'react';


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


function DishUpdateForm({ initialData }) {
  const [formData, setFormData] = useState({
    id: initialData.id,
    business_id: initialData.business_id,
    name: initialData.name,
    description: initialData.description,
    price: initialData.price,
    category_id: initialData.category_id,
    image_id: initialData.image_id,
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch(`/api/dish/business/${formData.business_id}/update/${formData.id}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    if (response.ok) {
      const updated = await response.json();
      alert('Dish updated successfully!');
      
    } else {
      console.error("Failed to update dish");
      alert('Failed to update dish. Please try again.');
    }
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
