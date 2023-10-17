import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addItemToCart, updateCartQuantity, deleteItemFromCart } from '../store/cart';  // Ensure these actions exist.

const CartContainer = () => {
  const [dishId, setDishId] = useState('');
  const [quantity, setQuantity] = useState(1);
  const [deliveryAddress, setDeliveryAddress] = useState('');
  const dispatch = useDispatch();
  const cartItems = useSelector(state => state.cart.current.items);
  const totalPrice = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);

  useEffect(() => {
    // Any cart setup or fetching can be added here.
  }, [dispatch]);

  const handleAddToCart = () => {
    dispatch(addItemToCart(dishId, quantity));
  };

  const handleUpdateQuantity = () => {
    dispatch(updateCartQuantity(dishId, quantity));
  };

  const handleDeleteFromCart = () => {
    dispatch(deleteItemFromCart(dishId));
  };

  const handleSubmitCart = async () => {
    const response = await fetch(`/api/cart/${cartItems[0].cart_id}/submit`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        total_price: totalPrice,
        delivery_address: deliveryAddress
      })
    });

    const data = await response.json();
    if (response.ok) {
      console.log("Cart submitted successfully!", data);
      // You can do more things here, like redirecting to a different page, or showing a success message.
    } else {
      console.error("Error submitting cart:", data.error);
    }
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
        <select value={dishId} onChange={(e) => setDishId(e.target.value)}>
          {/* Replace this with a list of all available dishes */}
          <option value="">Select a dish</option>
        </select>
        <input type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)} />
        <button onClick={handleAddToCart}>Add to Cart</button>
        <button onClick={handleUpdateQuantity}>Update Quantity</button>
      </div>

      {/* Submit Cart */}
      <div>
        <label>
          Delivery Address:
          <input type="text" value={deliveryAddress} onChange={(e) => setDeliveryAddress(e.target.value)} />
        </label>
        <button onClick={handleSubmitCart}>Submit Cart</button>
      </div>
    </aside>
  );
}

export default CartContainer;
