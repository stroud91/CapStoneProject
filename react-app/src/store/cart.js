const SET_CART = "cart/SET_CART";
const ADD_ITEM = "cart/ADD_ITEM";
const SUBMIT_CART = "cart/SUBMIT_CART";
const REMOVE_ITEM = "cart/REMOVE_ITEM";

export const setCart = (cart) => ({
  type: SET_CART,
  payload: cart,
});

export const addItem = (item) => ({
  type: ADD_ITEM,
  payload: item,
});

export const submitCart = (cart) => ({
  type: SUBMIT_CART,
  payload: cart,
});

export const removeItem = (itemId) => ({
  type: REMOVE_ITEM,
  payload: itemId,
});

export const getCart = () => async (dispatch) => {
  const response = await fetch(`/api/cart/`)
  if ( response.ok) {
    const cart = await response.json();
    dispatch(setCart(cart));
  } else {
    console.error("Thunk Error: Failed to fetch cart");
  }
};

export const addItemToCart = (cart_id, dish_id, quantity) => async (dispatch) => {
  console.log("this is add item ", cart_id,dish_id,quantity)
  const response = await fetch(`/api/cart/${cart_id}/items`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ dish_id: dish_id, quantity: quantity }),
  });

  if (response.ok) {
    const item = await response.json();
    dispatch(addItem(item));
  } else {
    console.error("Thunk Error: Failed to add item to cart");
  }
};

export const checkoutCart = (cartId, totalPrice, deliveryAddress) => async (dispatch) => {
  const response = await fetch(`/cart/${cartId}/submit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ total_price: totalPrice, delivery_address: deliveryAddress }),
  });

  if (response.ok) {
    const cart = await response.json();
    dispatch(submitCart(cart));
  } else {
    console.error("Thunk Error: Failed to submit cart");
  }
};

export const deleteItemFromCart = (cartId, itemId) => async (dispatch) => {
  const response = await fetch(`/cart/${cartId}/items/${itemId}`, {
    method: "DELETE",
  });

  if (response.ok) {
    dispatch(removeItem(itemId));
  } else {
    console.error("Thunk Error: Failed to delete item from cart");
  }
};

const initialState = {
  current: null,
  items: []
};

const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_CART:
      return { ...state, current: action.payload };
    case ADD_ITEM:
      return { ...state, items: [...state.items, action.payload] };
    case SUBMIT_CART:
      return initialState;
    case REMOVE_ITEM:
      return {
        ...state,
        items: state.items.filter(item => item.id !== action.payload)
      };
    default:
      return state;
  }
};

export default cartReducer;
