import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { fetchOneBusiness, getAllBusinesses } from '../../store/business';
import { fetchReviewsForDish, createReview, updateReview, deleteReview } from '../../store/review';
import { getDishesForBusiness, getSingleDish, removeDishForBusiness } from '../../store/dish';
import { addItemToCart } from '../../store/cart';
import CreateReviewModal from '../CreateReviewModal';
import EditReviewModal from '../UpdateReviewModal';
import DeleteReviewModal from '../DeleteReviewModal';
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import addToCart from '../CartComponent';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import LoadingAnimation from '../Loading';

function DishDetail() {
    const dispatch = useDispatch();
    const { id } = useParams();
    const { setModalContent, closeModal } = useModal();
    const history = useHistory()
    const [loading, setLoading] = useState(true);

    const currentUser = useSelector(state => state.session.user);
    const currentDish = useSelector(state => state.dish.current);

    const currentReviews = useSelector(state => state.review.reviewsForDish);

    const currentBusiness = useSelector(state => state.business.list).find(biz => biz.id === currentDish.business_id);


    useEffect(() => {

        async function fetchData() {
            setLoading(true);
            await dispatch(getSingleDish(id));
            await dispatch(fetchReviewsForDish(id));
            await dispatch(getAllBusinesses());

            setTimeout(() => {
                setLoading(false);
              }, 100);
        }
        fetchData();
    }, [dispatch, id ]);

    const handleAddToCart = () => {

        if (currentDish) {
            dispatch(addItemToCart(currentDish.id, 1));
            
        }
    }

    const handleEditDish = async (business_id, id) => {
        // if (!currentDish) return;
        // await dispatch(removeDishForBusiness(currentDish.business_id, dishId));
        history.push(`/business/${currentBusiness.id}/update-dish/${id}`)
    };

    const handleDeleteDish = async (dishId) => {
        if (!currentDish) return;
        await dispatch(removeDishForBusiness(currentDish.business_id, dishId));
    };

    if (loading) {
        return <div><LoadingAnimation /></div>;
      }

    return (
        <div className="dishDetail-container">

            <img src={currentDish.image_id} alt={currentDish.name} className="dishDetail-image" />
            <h3 className="dishDetail-name">{currentDish.name}</h3>
            <p className="dishDetail-description">{currentDish.description}</p>
            <span className="dishDetail-price">${currentDish.price.toFixed(2)}</span>
            {currentUser && (<button onClick={handleAddToCart}>Add to Cart</button>)}
            {currentUser && currentUser.id === currentBusiness.owner_id && (
                <div className="dishDetail-buttons">
                    {/* <Link to={`/business/${currentBusiness.id}/update-dish/${id}`} className="dishDetail-delete-button">Edit</Link> */}
                    <button className="dishDetail-delete-button" onClick={() => handleEditDish(currentBusiness.id,id)}>Edit</button>
                    <button className="dishDetail-delete-button" onClick={() => handleDeleteDish(currentDish.id)}>Delete</button>
                </div>
            )}

            {currentUser && currentUser.id !== currentBusiness.owner_id && (
                <div className="dishDetail-userActions">
                    <div className="dishDetail-postReview">
                        {currentUser &&
                         currentUser.id !== currentBusiness.owner_id &&
                         !currentReviews.some(review => review.user_id === currentUser.id) && (
                            <OpenModalButton
                                buttonText="Add a review"
                                modalComponent={<CreateReviewModal id={id} currentUser={currentUser.id} />}
                                id="dishDetail-postReview-button"
                            />

                        )}
                    </div>
                </div>
            )}

            <div className="dishDetail-reviews">
                <h4 className="dishDetail-reviewsTitle">Reviews</h4>
                {currentReviews.map(review => (
                    <div key={review.id} className="dishDetail-reviewItem">
                        <h5 className="dishDetail-reviewUserName">{review.user_name}</h5>
                        <p className="dishDetail-reviewComment">{review.comment}</p>
                        <span className="dishDetail-reviewRating">Rating: {review.rating}</span>

                        {currentUser && currentUser.id === review.user_id && (
                            <div className="dishDetail-reviewButtons">
                                <OpenModalButton
                                    buttonText="Edit"
                                    modalComponent={<EditReviewModal id={id} review={review} />}
                                    id="dishDetail-reviewEdit-button"
                                />
                                <OpenModalButton
                                    buttonText="Delete"
                                    modalComponent={<DeleteReviewModal id={id} review={review.id} />}
                                    id="dishDetail-reviewDelete-button"
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
