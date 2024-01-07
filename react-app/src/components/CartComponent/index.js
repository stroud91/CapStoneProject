import React, { useEffect } from 'react';
import { useDispatch, useSelector, history } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { getCart, addItemToCart, updateCartItem, deleteItemFromCart, submitCartThunk } from '../../store/cart';
import { getAllDishes } from '../../store/dish';

const Cart = () => {
    const dispatch = useDispatch();
    const history = useHistory();

    const cartItems = useSelector(state => state.cart.items);
    console.log("this is cartItems", cartItems)
    const dishes = useSelector(state => state.dish.list);

    useEffect(() => {
        dispatch(getAllDishes());
        dispatch(getCart());
        console.log("Cart items: ", cartItems);
        const totalPrice = getTotalPrice();
        console.log("Total Price: ", totalPrice);
    }, [dispatch]);

    const getDishDetails = (dishId) => dishes.find(dish => dish.id === dishId);

    const handleAddToCart = (dish) => {
        dispatch(addItemToCart(dish.id, 1));
    };

    const handleUpdateQuantity = async (itemId, newQuantity) => {
        if (newQuantity > 0) {
            await dispatch(updateCartItem(itemId, newQuantity));
            dispatch(getCart());
        }
    };


    const handleRemoveItem = async (itemId) => {
        await dispatch(deleteItemFromCart(itemId));
        dispatch(getCart());
    };


    const handleSubmitCart = async () => {
        await dispatch(submitCartThunk());
        alert("Order Submitted! Thank you for your purchase!");
        history.push("/");
    };


    const getTotalPrice = () => {

        if (Array.isArray(cartItems.items) && cartItems.items.length > 0) {
            return cartItems.items.reduce((total, item) => {
                const dishDetails = getDishDetails(item.dish_id);
                return total + (dishDetails?.price * item.quantity || 0);
            }, 0);
        }
        return 0;
    };


    return (
        <div className="cart-container">
            <h2>Your Cart</h2>
            <div className="cart-items">
                {cartItems && cartItems.items && cartItems.items.length > 0 ? (
                    cartItems.items.map(item => {
                        const dishDetails = getDishDetails(item.dish_id);
                        return (
                            <div className="cart-item" key={item.item_id}>
                                <img src={dishDetails?.image_url} alt={dishDetails?.name} className="cart-item-image" />
                                <div className="cart-item-details">
                                    <div className="cart-item-name">{dishDetails?.name}</div>
                                    <div className="cart-item-price">${dishDetails?.price.toFixed(2)}</div>
                                    <div className="cart-item-quantity">
                                        <button onClick={() => handleUpdateQuantity(item.item_id, item.quantity - 1)}>-</button>
                                        <span>{item.quantity}</span>
                                        <button onClick={() => handleUpdateQuantity(item.item_id, item.quantity + 1)}>+</button>
                                    </div>
                                    <button className="cart-item-remove" onClick={() => handleRemoveItem(item.item_id)}>Remove</button>
                                </div>
                            </div>
                        );
                    })
                ) : (
                    <p>Your cart is empty.</p>
                )}
            </div>
            <div className="cart-total">
                <div>Total: ${getTotalPrice().toFixed(2)}</div>
                <button className="cart-submit" onClick={() => handleSubmitCart()}>Checkout</button>
            </div>
        </div>
    );
}

export default Cart;
