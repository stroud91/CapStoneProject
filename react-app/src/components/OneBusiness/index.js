import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import CreateReviewModal from "../CreateReviewModal";
import OpenModalButton from "../OpenModalButton";
import DeleteReviewModal from "../DeleteReviewModal";
import UpdateReviewModal from "../UpdateReviewModal";
import { fetchOneBusiness} from "../../store/business";
import {setDishesForBusiness} from "../../store/dish"
import { useParams, useHistory } from "react-router-dom";
import { deleteBusiness } from "../../store/business";
import { fetchSingleBusinessReviews } from "../../store/review";
import noImage from "../../images/no-image.png";
import "./OneBusiness.css";
import DeleteModal from "../DeleteBusinessModal";

const changeDate = (date) => {
    const newDate = new Date(date);
    const options = { day: 'numeric', month: 'long', year: 'numeric' };
    return newDate.toLocaleString('en-US', options);
}

function Review({ review, user, businessId }) {
    return (
        <div key={review.id} className="individualReview">
            <p className="user-individual-review">
                {review.user_first_name} {review.user_last_name} posted on {changeDate(review.created_at)}:
            </p>
            <p>{review.review_body}</p>
            <p>
                {[...Array(review.rating)].map((_, index) => (
                    <i key={index} className="fa-solid fa-star"></i>
                ))}
            </p>
            {user && review.user_id === user.id && (
                <div className="reviewButtons">
                    <OpenModalButton
                        buttonText="Edit"
                        modalComponent={<UpdateReviewModal business_id={businessId} review={review} />}
                        id={"review-edit-button"}
                    />
                    <OpenModalButton
                        buttonText="Delete"
                        modalComponent={<DeleteReviewModal id={businessId} review={review.id} />}
                        id={"review-delete-button"}
                    />
                </div>
            )}
        </div>
    );
}

function Dish({ dish }) {
    return (
        <div className="dish-container">
            <img src={dish.imageUrl || noImage} alt={dish.name} className="dish-image" />
            <h3>{dish.name}</h3>
            <p>{dish.description}</p>
            <span>${dish.price.toFixed(2)}</span>
        </div>
    );
}

function BusinessDetail() {
    const history = useHistory();
    const dispatch = useDispatch();
    const { id } = useParams();

    const business = useSelector((state) => state.business.selectedBusiness);
    const dishes = useSelector((state) => state.business.dishes);
    const currentUser = useSelector((state) => state.session.user);
    const reviews = useSelector((state) => state.review.allReviews);
    const user = currentUser;


    const handleEdit = () => {
        history.push(`/business/${business.id}/edit`);
      };

    const handleDelete = async () => {

        const confirmed = window.confirm("Are you sure you want to delete this business?");
        if (confirmed) {
            try {
                await dispatch(deleteBusiness(id));
                history.push('/');
            } catch (error) {
                console.error("Failed to delete the business:", error);
            }
        }
    };


    useEffect(() => {

        dispatch(fetchOneBusiness(id));


        dispatch(setDishesForBusiness(id));


        dispatch(fetchSingleBusinessReviews(id));

    }, [dispatch, id]);


    const renderedReviews = reviews?.restaurant_reviews.map((review) => (
        <Review key={review.id} review={review} user={user} businessId={id} />
    )).reverse();

    const renderedDishes = dishes?.map(dish => (
        <Dish key={dish.id} dish={dish} />
    ));

    return (
        <div>
            <h1>{business.name}</h1>



            {/* Business Details */}
            <div className="business-detail-container">

                {/* Side Panel with Contact Info */}
                <div className="business-side-panel">
                    {/* ... Contact Information ... */}
                </div>

                {/* Main Business Info */}
                <div className="business-info">
                    {/* ... Main Business Information ... */}

                    {/* Conditionally Render Edit & Delete Buttons */}
                    {currentUser && currentUser.id === business.owner_id && (
                      <div className="business-buttons-conditional">
                    <button
                     className="edit-business-button"
                      onClick={() => handleEdit(business.id)}
                    >
                    Edit
                    </button>
                    <OpenModalButton
                    buttonText="Delete"
                    modalComponent={<DeleteModal bus_data={business} />}
                    id={"delete-business-button"}
                    />
                </div>
                )}
                </div>
            </div>

            {/* Post Review */}
            <div className="postYourReview">
                {/* ... Conditionally Render Post Review Button ... */}
            </div>

            {/* Display Reviews */}
            {reviews && reviews.restaurant_reviews
                .map((review) => (
                    <div key={review.id} className="individualReview">
                        {/* ... Individual Review ... */}
                        <p className="user-individual-review">
                            {/* ... Reviewer's Name and Date ... */}
                        </p>
                        <p>{review.review_body}</p>
                        <p>
                            {/* ... Review Rating Stars ... */}
                        </p>
                        {user && review.user_id === user.id && (
                            <div className="reviewButtons">
                                {/* ... Edit and Delete Review Buttons ... */}
                            </div>
                        )}
                    </div>
                ))
                .reverse()
            }
        </div>
    );

}

export default BusinessDetail;
