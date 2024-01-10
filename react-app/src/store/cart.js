const SET_CART = "cart/SET_CART";
const ADD_ITEM = "cart/ADD_ITEM";
const SUBMIT_CART = "cart/SUBMIT_CART";
const REMOVE_ITEM = "cart/REMOVE_ITEM";
const CART_ERROR = "cart/CART_ERROR";
const UPDATE_ITEM = "cart/UPDATE_ITEM";


export const setCart = (cart) => ({
  type: SET_CART,
  payload: cart,
});

export const addItem = (item) => ({
  type: ADD_ITEM,
  payload: item,
});

export const submitCart = () => ({
  type: SUBMIT_CART,
});

export const removeItem = (itemId) => ({
  type: REMOVE_ITEM,
  payload: itemId,
});

export const cartError = (error) => ({
  type: CART_ERROR,
  payload: error,
});

export const updateItem = (itemId, newQuantity) => ({
  type: UPDATE_ITEM,
  payload: { itemId, newQuantity },
});

export const getCart = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/cart/view`);
    if (response.ok) {
      const cart = await response.json();
      dispatch(setCart(cart));
    } else {
      throw new Error('Failed to fetch cart');
    }
  } catch (error) {
    console.error("Thunk Error:", error.message);
    dispatch(cartError(error.message));
  }
};

export const addItemToCart = (dish_id, quantity) => async (dispatch) => {
  console.log("add to cart logs from thunk", dish_id, quantity)
  try {
    const response = await fetch(`/api/cart/add`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ dish_id, quantity }),
    });

    if (response.ok) {
      const item = await response.json();
      dispatch(addItem(item));
    } else {
      throw new Error('Failed to add item to cart');
    }
  } catch (error) {
    console.error("Thunk Error:", error.message);
    dispatch(cartError(error.message));
  }
};


export const submitCartThunk = () => async (dispatch) => {
  try {
      const response = await fetch(`/api/cart/submit`, {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          credentials: 'include',
      });
      if (response.ok) {
          dispatch(submitCart());
      } else {
          const error = await response.json();
          dispatch(cartError(error.message));
      }
  } catch (error) {
      console.error("Thunk Error:", error.message);
      dispatch(cartError(error.message));
  }
};


export const updateCartItem = (cartItemId, newQuantity) => async (dispatch) => {

  try {
    const response = await fetch(`/api/cart/update`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ cart_item_id: cartItemId, change: newQuantity }),
    });

    if (response.ok) {
      const message = await response.json();
      dispatch({
        type: UPDATE_ITEM,
        payload: { cartItemId, quantity: newQuantity }
      });

    } else {
      throw new Error('Failed to update item in cart');
    }
  } catch (error) {
    console.error("Thunk Error:", error.message);
    dispatch(cartError(error.message));
  }
};



export const deleteItemFromCart = (itemId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/cart/remove`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ cart_item_id: itemId }),
    });

    if (response.ok) {
      dispatch(removeItem(itemId));
    } else {
      throw new Error('Failed to delete item from cart');
    }
  } catch (error) {
    console.error("Thunk Error:", error.message);
    dispatch(cartError(error.message));
  }
};




const initialState = {
  current: null,
  items: [],
  error: null
};

const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_CART:
      return { ...state, items: action.payload, error: null };
    case ADD_ITEM:
      return { ...state, items: [...state.items, action.payload], error: null };
      case UPDATE_ITEM:
        return {
          ...state,
          items: state.items.map(item =>
            item.id === action.payload.id ? { ...item, ...action.payload } : item
          ),
          error: null
        };

        case SUBMIT_CART:
          return {
              ...state,
              items: [],
              current: null,
              error: null,
          };
    case REMOVE_ITEM:
      return {
        ...state,
        items: state.items.filter(item => item.id !== action.payload),
        error: null
      };
    case CART_ERROR:
      return { ...state, error: action.payload };
    default:
      return state;
  }
};

export default cartReducer;
