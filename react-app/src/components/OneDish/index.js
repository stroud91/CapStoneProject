import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import OpenModalButton from "../OpenModalButton";
import DeleteDishModal from "../DeleteDishModal";

import { fetchReviewsForDish } from '../../store/review';
import { getSingleDish, removeDishForBusiness } from '../../store/dish';
function DishDetail() {
    const dispatch = useDispatch();
    const { id } = useParams();
    const [dish, setDish] = useState(null);
    const [reviews, setReviews] = useState([]);
    const currentUser = useSelector(state => state.session.user);
    const currentDish = useSelector(state => state.dish.current);
    const currentReviews = useSelector(state => state.review.reviewsForDish);
    const business = useSelector(state => state.business.selectedBusiness);
    console.log("this is current dish",currentDish)
    const [loading, setLoading] = useState(true);
    useEffect(() => {


        async function fetchData() {
            await dispatch(getSingleDish(id));
            await dispatch(fetchReviewsForDish(id));
            setLoading(false);
        }
        fetchData();
    }, [dispatch, id]);

    const handleDelete = async (dishId) => {
        if (!dish) return;
        await dispatch(removeDishForBusiness(dish.business_id, dishId));
    };


    if (!currentDish) return <div>Loading...</div>;
    if (!currentReviews) return <div>Loading...</div>;
    
    return (
        <div className="dish-detail-container">
            <img src={currentDish.image_id} alt={currentDish.name} className="dish-image" />
            <h3>{currentDish.name}</h3>
            <p>{currentDish.description}</p>
            <span>${currentDish.price.toFixed(2)}</span>

            {currentUser && currentUser.id === business.owner_id && (
                <div className="dish-buttons">
                     <Link to={`/dish/${dish.id}/edit`} className="edit-button">
                       Edit
                     </Link>
                    <OpenModalButton
                        buttonText="Delete"
                        modalComponent={<DeleteDishModal id={dish.id} onDelete={() => handleDelete(dish.id)} businessId={dish.business_id} />}
                        id={`dish-delete-button-${dish.id}`}
                    />
                </div>
            )}

            <div className="dish-reviews">
                <h4>Reviews</h4>
                {currentReviews.map(review => (
                    <div key={review.id} className="review">
                        <h5>{review.user_name}</h5>
                        <p>{review.comment}</p>
                        <span>Rating: {review.rating}</span>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default DishDetail;
