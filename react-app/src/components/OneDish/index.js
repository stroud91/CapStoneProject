import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { fetchOneBusiness } from '../../store/business';
import { fetchReviewsForDish, createReview, updateReview, deleteReview } from '../../store/review';
import { getDishesForBusiness, getSingleDish, removeDishForBusiness } from '../../store/dish';
import { addItemToCart } from '../../store/cart';
import CreateReviewModal from '../CreateReviewModal';
import EditReviewModal from '../UpdateReviewModal';
import DeleteReviewModal from '../DeleteReviewModal';
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";

function DishDetail() {

    const dispatch = useDispatch();
    const { id } = useParams();
    const { setModalContent, closeModal } = useModal();
    const [loading, setLoading] = useState(true);

    const currentUser = useSelector(state => state.session.user);
    const currentDish = useSelector(state => state.dish.current);
    console.log("current dish", currentDish)
    const currentReviews = useSelector(state => state.review.reviewsForDish);
    console.log("current reviews", currentReviews)
    const business = useSelector(state => state.business.selectedBusiness);

    useEffect(() => {

        async function fetchData() {
           await dispatch(getSingleDish(id));
           await dispatch(fetchReviewsForDish(id));
           await dispatch(fetchOneBusiness(currentDish.business_id));
           setLoading(false);
        }
        fetchData();
    }, [dispatch, id,currentDish.business_id]);

    const handleAddToCart = (dishId) => {
        dispatch(addItemToCart(dishId));
    }

    const handleDeleteDish = async (dishId) => {
        if (!currentDish) return;
        await dispatch(removeDishForBusiness(currentDish.business_id, dishId));
    };

    if (loading) return <div>Loading...</div>;

    return (
        <div className="dish-detail-container">
            <img src={currentDish.image_id} alt={currentDish.name} className="dish-image" />
            <h3>{currentDish.name}</h3>
            <p>{currentDish.description}</p>
            <span>${currentDish.price.toFixed(2)}</span>

            {currentUser && currentUser.id === business.owner_id && (
                <div className="dish-buttons">
                    <Link to={`/dish/${id}/update`} className="edit-button">Edit</Link>
                    <button onClick={() => handleDeleteDish(currentDish.id)}>Delete</button>
                </div>
            )}

            {currentUser && currentUser.id !== business.owner_id && (
                <div className="dish-user-actions">
                    <button className="add-cart-btn" onClick={() => handleAddToCart(currentDish.id)}>Add to Cart</button>
                    <div className="postYourReview">
                    {currentUser &&
                     currentUser.id !== business.owner_id &&
                      !currentReviews.some(review => review.user_id === currentUser.id) && (
                    <OpenModalButton
                     buttonText="Add a review"
                     modalComponent={<CreateReviewModal id={id} currentUser={currentUser.id} />}
                     id={"post-review-button"}
  />
)}

      </div>
                </div>
            )}

            <div className="dish-reviews">
                <h4>Reviews</h4>
                {currentReviews.map(review => (
                    <div key={review.id} className="review">
                        <h5>{review.user_name}</h5>
                        <p>{review.comment}</p>
                        <span>Rating: {review.rating}</span>

                        {currentUser && currentUser.id === review.user_id && (
                            <div className="reviewButtons">
                                <OpenModalButton
                                buttonText="Edit"
                                modalComponent={
                                <EditReviewModal id={id} review={review} />
                                }
                                id={"review-edit-button"}
                                />
                                <OpenModalButton
                                 buttonText="Delete"
                                 modalComponent={
                                <DeleteReviewModal id={id} review={review.id} />
                                 }
                                 id={"review-delete-button"}
                               />
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default DishDetail;
