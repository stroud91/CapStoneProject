
const SET_ALL_DISHES = "dish/SET_ALL_DISHES";
const SET_DISHES_FOR_BUSINESS = "dish/SET_DISHES_FOR_BUSINESS";
const SET_SINGLE_DISH = "dish/SET_SINGLE_DISH";
const ADD_DISH = "dish/ADD_DISH";
const UPDATE_DISH = "dish/UPDATE_DISH";
const DELETE_DISH = "dish/DELETE_DISH";
const SET_TOP_RATED_DISHES = 'SET_TOP_RATED_DISHES';
const SET_TOP_ORDERED_DISHES = 'SET_TOP_ORDERED_DISHES';

export const setTopRatedDishes = (dishes) => {
  return {
    type: SET_TOP_RATED_DISHES,
    dishes,
  };
};

export const setTopOrderedDishes = (dishes) => {
  return {
    type: SET_TOP_ORDERED_DISHES,
    dishes,
  };
};

export const setAllDishes = (dishes) => ({
  type: SET_ALL_DISHES,
  payload: dishes,
});

export const setDishesForBusiness = (dishes) => ({
  type: SET_DISHES_FOR_BUSINESS,
  payload: dishes,
});

export const setSingleDish = (dish) => ({
  type: SET_SINGLE_DISH,
  payload: dish
});

export const addDish = (dish) => ({
  type: ADD_DISH,
  payload: dish,
});

export const updateDish = (dish) => ({
  type: UPDATE_DISH,
  payload: dish,
});

export const deleteDish = (id) => ({
  type: DELETE_DISH,
  payload: id,
});

export const getAllDishes = () => async (dispatch) => {
  const response = await fetch(`/api/menu`);
  if (response.ok) {
    const dishes = await response.json();
    dispatch(setAllDishes(dishes));
  } else {
    console.error("Thunk Error: Failed to fetch dishes");
  }
};

export const getDishesForBusiness = (businessId) => async (dispatch) => {
  const response = await fetch(`/api/menu/business/${businessId}`);
  if (response.ok) {
    const dishes = await response.json();
    dispatch(setDishesForBusiness(dishes));
  } else {
    console.error("Thunk Error: Failed to fetch dishes for business");
  }
};

export const getSingleDish = (dishId) => async (dispatch) => {
  const response = await fetch(`/api/menu/${dishId}`);
  if (response.ok) {
    const dish = await response.json();
    dispatch(setSingleDish(dish));
  } else {
    console.error("Thunk Error: Failed to fetch dish");
  }
};

export const createDishForBusiness = (businessId, dish) => async (dispatch) => {
  const response = await fetch(`/api/menu/business/${businessId}/add`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dish),
  });
  if (response.ok) {
    const newDish = await response.json();
    dispatch(addDish(newDish));
  } else {
    console.error("Thunk Error: Failed to add dish");
  }
};

export const editDishForBusiness = (businessId, dishId, updatedDish) => async (dispatch) => {
  const response = await fetch(`/api/menu/business/${businessId}/update/${dishId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(updatedDish),
  });
  if (response.ok) {
    const updated = await response.json();
    dispatch(updateDish(updated));
  } else {
    console.error("Thunk Error: Failed to update dish");
  }
};

export const removeDishForBusiness = (businessId, dishId) => async (dispatch) => {
  const response = await fetch(`/api/menu/business/${businessId}/dish/${dishId}`, {
    method: 'DELETE',
  });
  if (response.ok) {
    dispatch(deleteDish(dishId));
  } else {
    console.error("Thunk Error: Failed to delete dish");
  }
};

export const fetchTopRatedDishes = () => {
  return async (dispatch) => {
    const response = await fetch('api/menu/top-rated');
    if (response.ok) {
      const dishes = await response.json();
      dispatch(setTopRatedDishes(dishes));
    }
  };
};

export const fetchTopOrderedDishes = () => {
  return async (dispatch) => {
    const response = await fetch('api/menu/top-ordered');
    if (response.ok) {
      const dishes = await response.json();
      dispatch(setTopOrderedDishes(dishes));
    }
  };
};


const initialState = {
  list: [],
  current: null,
  dishesForBusiness: [],
  topRated: [],
  topOrdered: []
};


const dishReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_ALL_DISHES:
      return {
        ...state,
        list: action.payload,
      };
    case SET_DISHES_FOR_BUSINESS:
      return {
        ...state,
        dishesForBusiness: action.payload,
      };
    case SET_SINGLE_DISH:
      return { ...state, current: action.payload };
    case ADD_DISH:
      return { ...state, list: [...state.list, action.payload] };
    case UPDATE_DISH:
      return {
        ...state,
        list: state.list.map((dish) =>
          dish.id === action.payload.id ? action.payload : dish
        ),
      };
    case DELETE_DISH:
      return {
        ...state,
        list: state.list.filter((dish) => dish.id !== action.payload),
      };
    case SET_TOP_RATED_DISHES:
        return {
          ...state,
          topRated: action.dishes,
        };
    case SET_TOP_ORDERED_DISHES:
        return {
          ...state,
          topOrdered: action.dishes,
        };
    default:
      return state;
  }
};

export default dishReducer;
