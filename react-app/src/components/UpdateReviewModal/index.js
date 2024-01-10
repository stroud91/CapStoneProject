import { useDispatch, useSelector } from "react-redux";
import { useState, useEffect } from "react";
import { useModal } from "../../context/Modal";
import "./UpdateReviewModal.css";
import StarsRating from "./StarsRating";
import { updateReview } from "../../store/review";
import { fetchReviewsForDish } from "../../store/review";

function EditReviewModal({ id, review }) {

  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const [errors, setErrors] = useState({});
  const [stars, setStars] = useState(review.rating);
  const [comment, setComment] = useState(review.comment);
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

    const updatedReview = {
      user_id: userId,
      comment: comment,
      rating: stars
    };

    dispatch(updateReview(review.id, updatedReview))
      .then(() => {
        dispatch(fetchReviewsForDish(id));
        closeModal();
      });
  };

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
        {errors.stars && <p>{errors.stars}</p>}
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
