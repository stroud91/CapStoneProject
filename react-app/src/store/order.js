// Action Types
const SET_ORDERS = "order/SET_ORDERS";
const SET_ORDER_DETAILS = "order/SET_ORDER_DETAILS";
const ADD_ORDER = "order/ADD_ORDER";
const REMOVE_ORDER = "order/REMOVE_ORDER";
const UPDATE_ORDER_STATUS = "order/UPDATE_ORDER_STATUS";

// Action Creators
export const setOrders = (orders) => ({
  type: SET_ORDERS,
  payload: orders,
});

export const setOrderDetails = (details) => ({
  type: SET_ORDER_DETAILS,
  payload: details,
});

export const addOrder = (order) => ({
  type: ADD_ORDER,
  payload: order,
});

export const removeOrder = (id) => ({
  type: REMOVE_ORDER,
  payload: id,
});

export const updateOrderStatus = (order) => ({
  type: UPDATE_ORDER_STATUS,
  payload: order,
});

// Thunks
export const getUserOrders = () => async (dispatch) => {
  const response = await fetch("/api/user/orders");
  if (response.ok) {
    const data = await response.json();
    dispatch(setOrders(data));
  } else {
    console.error("Thunk Error: Failed to fetch user orders");
  }
};

export const getBusinessOrders = (businessId) => async (dispatch) => {
  const response = await fetch(`/api/business/${businessId}/orders`);
  if (response.ok) {
    const data = await response.json();
    dispatch(setOrders(data));
  } else {
    console.error("Thunk Error: Failed to fetch business orders");
  }
};

export const submitCartAsOrder = (cartId, orderData) => async (dispatch) => {
    const response = await fetch(`/api/cart/${cartId}/submit`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(orderData),
    });

    if (response.ok) {
      const newOrder = await response.json();
      dispatch(addOrder(newOrder));
      return newOrder;
    } else {
      const errorData = await response.json();
      console.error("Thunk Error: Failed to submit cart as order", errorData.error);
      throw new Error(errorData.error);
    }
  };


// Initial State
const initialState = {
  orders: [],
  orderDetails: [],
};

// Reducer
const orderReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_ORDERS:
      return { ...state, orders: action.payload };
    case SET_ORDER_DETAILS:
      return { ...state, orderDetails: action.payload };
    case ADD_ORDER:
      return { ...state, orders: [...state.orders, action.payload] };
    case REMOVE_ORDER:
      return { ...state, orders: state.orders.filter(order => order.id !== action.payload) };
    case UPDATE_ORDER_STATUS:
      return {
        ...state,
        orders: state.orders.map(order => order.id === action.payload.id ? action.payload : order)
      };
    default:
      return state;
  }
};

export default orderReducer;
