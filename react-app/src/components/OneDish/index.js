import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import OpenModalButton from "../OpenModalButton";
import DeleteDishModal from "../DeleteDishModal";

import { fetchSingleBusinessReviews } from '../../store/review';
import { getSingleDish, removeDishForBusiness } from '../../store/dish';
function DishDetail() {
    const dispatch = useDispatch();
    const { dishId } = useParams();
    const [dish, setDish] = useState(null);
    const [reviews, setReviews] = useState([]);
    const currentUser = useSelector(state => state.session.user);

    useEffect(() => {

        const fetchDish = async () => {
            const fetchedDish = await dispatch(getSingleDish(dishId));
            setDish(fetchedDish);
        }

        const fetchReviews = async () => {
            const fetchedReviews = await dispatch(fetchSingleBusinessReviews(dishId));
            setReviews(fetchedReviews);
        }

        fetchDish();
        fetchReviews();
    }, [dispatch, dishId]);

    const handleDelete = async (dishId) => {
        if (!dish) return;
        await dispatch(removeDishForBusiness(dish.business_id, dishId));
    };


    if (!dish) return <div>Loading...</div>;

    return (
        <div className="dish-detail-container">
            <img src={dish.image_id} alt={dish.name} className="dish-image" />
            <h3>{dish.name}</h3>
            <p>{dish.description}</p>
            <span>${dish.price.toFixed(2)}</span>

            {currentUser && currentUser.id === dish.business_id && (
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
                {reviews.map(review => (
                    <div key={review.id} className="review">
                        <h5>{review.title}</h5>
                        <p>{review.content}</p>
                        <span>Rating: {review.rating}</span>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default DishDetail;
