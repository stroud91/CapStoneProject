import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {getCart, addItemToCart, deleteItemFromCart, checkoutCart } from '../../store/cart';  // Ensure these actions exist.
import { getSingleDish } from '../../store/dish';
const CartContainer = () => {

  const [dish_id, setDishId] = useState('');
  const [quantity, setQuantity] = useState(1);
  const [delivery_address, setDeliveryAddress] = useState('');
  const [loading, setLoading] = useState(true);
  const dispatch = useDispatch();
  const cartItems = useSelector(state => state.cart.current.items);
  const total_price = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);
  const cart_id = useSelector(state => state.cart.current);
  const currentUser = useSelector(state => state.session.user);
  console.log("current user", currentUser)
  const currentDish = useSelector(state => state.dish.current);
  console.log("current Dish", currentDish)


  useEffect(() => {
    async function fetchData() {
      await dispatch(getCart(currentUser.id))
      await dispatch(getSingleDish(currentDish.id));
      setLoading(false);
  }
  fetchData();
  }, [dispatch]);

  if (loading) return <div>Loading...</div>;

  const handleAddToCart = () => {
    dispatch(addItemToCart(cart_id, dish_id, quantity));
  };

  const handleDeleteFromCart = () => {
    dispatch(deleteItemFromCart(dish_id));
  };

  const handleSubmitCart = async () => {
    dispatch(checkoutCart(cart_id, total_price));
  };

  return (
    <aside>
      <h2>Cart</h2>

      {/* List out cart items */}
      <ul>
        {cartItems.map(item => (
          <li key={item.dish_id}>
            {item.dish.name} - {item.quantity}
            <button onClick={() => handleDeleteFromCart(item.dish_id)}>Delete</button>
          </li>
        ))}
      </ul>

      {/* Add to Cart */}
      <div>
      <select value={dish_id} onChange={(e) => setDishId(e.target.value)}>
    <option value="">Select a dish</option>
    {currentDish.map(dish => (
      <option value={dish.id}>{dish.name}</option>
    ))}
</select>

        <input type="number" value={1} onChange={(e) => setQuantity(e.target.value)} />
        <button onClick={handleAddToCart}>Add to Cart</button>
      </div>

      {/* Submit Cart */}
      <div>
        <label>
          Delivery Address:
          <input type="text" value={delivery_address} onChange={(e) => setDeliveryAddress(e.target.value)} />
        </label>
        <button onClick={handleSubmitCart}>Submit Cart</button>
      </div>
    </aside>
  );
}

export default CartContainer;
