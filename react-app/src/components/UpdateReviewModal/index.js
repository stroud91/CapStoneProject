import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { useParams } from "react-router-dom";
import "./UpdateReviewModal.css";
import StarsRating from "./StarsRating";
import { editedReview } from "../../store/review";
import { fetchOneBusiness } from "../../store/business";
import { fetchSingleBusinessReviews } from "../../store/review";

function EditReviewModal({ business_id, review }) {

  const dispatch = useDispatch();
  const history = useHistory();
  const business = useSelector((state) => state.business.selectedBusiness);
  const user = useSelector((state) => state.session.user);
  const reviews = useSelector((state) => state.reviews.reviews);
  const [errors, setErrors] = useState({});
  const [stars, setStars] = useState(review.rating);
  const [comment, setComment] = useState(review.review_body);
  const [formDisabled, setFormDisabled] = useState(true);
  const { closeModal } = useModal();

  useEffect(() => {
    const errors = {};
    if (stars && stars < 1) {
      errors.stars = "Please input a star rating";
    }
    if (comment && comment.length < 10) {
      errors.comment = "Comment needs a minimum of 10 characters";
    }
    setErrors(errors);
  }, [stars, comment]);

  useEffect(() => {
    if (!stars || !comment || stars < 1 || comment.length < 10) {
      setFormDisabled(true);
    } else {
      setFormDisabled(false);
    }
  }, [dispatch, stars, comment]);

  const onChange = (stars) => {
    setStars(stars);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setErrors({});
    const userId = user ? user.id : null;

    const editedReview = { comment, stars };


    dispatch(editedReview(review.id, editedReview))
      .then(() => {
        dispatch(fetchOneBusiness(business_id));
        dispatch(fetchSingleBusinessReviews(business_id));
        closeModal();
      })

  };

  if (!business) return <div>Loading...</div>;
  return (
    <div id="editReviewContainer">
      <div className="editReviewHeading">Edit Your Review</div>
      <label>
        <input
          type="text"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          className="comment-input"
          placeholder="Edit your review here..."
        />
      </label>
      {errors.comment && <p>{errors.comment}</p>}
      <div className="rating-input">
        <StarsRating disabled={false} stars={stars} onChange={onChange} />
        <div>Stars</div>
        {errors.rating && <p>{errors.rating}</p>}
      </div>
      <button
        onClick={handleSubmit}
        className={formDisabled ? "submit-button-inactive" : "submit-button"}
        type="submit"
        disabled={formDisabled}
      >
        Save Changes
      </button>
    </div>
  );
}

export default EditReviewModal;
