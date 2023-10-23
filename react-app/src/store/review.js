// Constants
const GET_ALL_BUSINESS_REVIEWS = 'GET_ALL_BUSINESS_REVIEWS';
const GET_CURRENT_USER_REVIEWS = 'GET_CURRENT_USER_REVIEWS';
const GET_SINGLE_BUSINESS_REVIEWS = 'GET_SINGLE_BUSINESS_REVIEWS';
const CREATE_REVIEW = 'CREATE_REVIEW';
const DELETE_REVIEW = 'DELETE_REVIEW';
const EDIT_REVIEW = 'EDIT_REVIEW';
const SET_REVIEWS_FOR_DISH = "SET_REVIEWS_FOR_DISH";


// Action Creators
const getBusinessReviews = reviews => ({
    type: GET_ALL_BUSINESS_REVIEWS,
    reviews
});

const getSingleBusinessReviews = reviews => ({
    type: GET_SINGLE_BUSINESS_REVIEWS,
    reviews
});

const getUserReviews = reviews => ({
    type: GET_CURRENT_USER_REVIEWS,
    reviews
});

const createReviewAction = review => ({
    type: CREATE_REVIEW,
    review
});

const deleteReviewAction = reviewId => ({
    type: DELETE_REVIEW,
    reviewId
});

const editReviewAction = review => ({
    type: EDIT_REVIEW,
    review
});

const setReviewsForDish = reviews => ({
    type: SET_REVIEWS_FOR_DISH,
    reviews
});

// Thunks
export const fetchAllReviews = () => async dispatch => {
    try {
        const response = await fetch('/api/review');

        if (!response.ok) {
            const errorData = await response.json();
            throw errorData;
        }

        const reviews = await response.json();
        dispatch(getBusinessReviews(reviews));
    } catch (err) {
        console.error('Error fetching all reviews:', err);
    }
};

export const fetchSingleBusinessReviews = businessId => async dispatch => {
    try {
        const response = await fetch(`/api/review/business/${businessId}`);

        if (!response.ok) {
            const errorData = await response.json();
            throw errorData;
        }

        const reviews = await response.json();
        dispatch(getSingleBusinessReviews(reviews));
    } catch (err) {
        console.error('Error fetching reviews for business:', err);
    }
};

export const fetchReviewsForDish = (dishId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/review/dish/${dishId}`);

        if (!response.ok) {
            const errorData = await response.json();
            throw errorData;
        }

        const reviews = await response.json();
        dispatch(setReviewsForDish(reviews));
    } catch (err) {
        console.error('Error fetching reviews for dish:', err);
    }
};

export const fetchUserReviews = () => async dispatch => {
    try {
        const response = await fetch('/api/review/user');

        if (!response.ok) {
            const errorData = await response.json();
            throw errorData;
        }

        const reviews = await response.json();
        dispatch(getUserReviews(reviews));
    } catch (err) {
        console.error('Error fetching user reviews:', err);
    }
};

export const createReview = (reviewData) => async dispatch => {
    try {
        const response = await fetch(`/api/review/create`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(reviewData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw errorData;
        }

        const newReview = await response.json();
        dispatch(createReviewAction(newReview));
    } catch (err) {
        console.error('Error creating review:', err);
    }
};

export const updateReview = (reviewId, updatedData) => async dispatch => {
    try {
        const response = await fetch(`/api/review/${reviewId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw errorData;
        }

        const updatedReview = await response.json();
        dispatch(editReviewAction(updatedReview));
    } catch (err) {
        console.error('Error updating review:', err);
    }
};

export const deleteReview = reviewId => async dispatch => {
    try {
        const response = await fetch(`/api/review/${reviewId}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw errorData;
        }

        dispatch(deleteReviewAction(reviewId));
    } catch (err) {
        console.error('Error deleting review:', err);
    }
};


const initialState = {
    allBusinessReviews: [],
    singleBusinessReviews: [],
    userReviews: [],
    reviewsForDish: [],
};

const reviewReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALL_BUSINESS_REVIEWS:
            return { ...state, allBusinessReviews: action.reviews };
        case GET_SINGLE_BUSINESS_REVIEWS:
            return { ...state, singleBusinessReviews: action.reviews };
        case GET_CURRENT_USER_REVIEWS:
            return { ...state, userReviews: action.reviews };
        case SET_REVIEWS_FOR_DISH:
            return {
                ...state,
                reviewsForDish: action.reviews
                };
        case CREATE_REVIEW:
            return {
                ...state,
                singleBusinessReviews: [...state.singleBusinessReviews, action.review]
            };
        case EDIT_REVIEW:
            return {
                ...state,
                singleBusinessReviews: state.singleBusinessReviews.map(
                    review => review.id === action.review.id ? action.review : review
                )
            };
        case DELETE_REVIEW:
            return {
                ...state,
                singleBusinessReviews: state.singleBusinessReviews.filter(
                    review => review.id !== action.reviewId
                )
            };
        default:
            return state;
    }
};

export default reviewReducer;
