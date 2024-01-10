import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { useParams } from "react-router-dom";
import "./CreateReviewModal.css";
import { createReview } from "../../store/review";
import StarsRating from "./StarsRating";
import { fetchReviewsForDish } from '../../store/review';
import { fetchSingleBusinessReviews } from "../../store/review";

function CreateReviewModal({ id, currentUser }) {

  const dispatch = useDispatch();
  const history = useHistory();
  const currentReviews = useSelector(state => state.review.reviewsForDish);
  const dish = useSelector(state => state.dish.current);
  

  const [errors, setErrors] = useState({});
  const [stars, setStars] = useState(0);
  const [comment, setComment] = useState("");
  const [formDisabled, setFormDisabled] = useState(true);
  const { closeModal } = useModal();

  useEffect(() => {
    dispatch(fetchReviewsForDish(id));
  }, [dispatch, id]);

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

    const userId = currentUser ? currentUser.id : null;
    const dishId = dish && dish.id ? dish.id : null;
    const submittedReview = {
      user_id: userId,
      comment: comment,
      rating: stars,
      dish_id: dishId
    };

    dispatch(createReview(submittedReview))
      .then(() => {
        dispatch(fetchReviewsForDish(id));

        closeModal();
      })
      .catch(async (res) => {
        const data = await res.json();
        if (data && data.errors) {
          setErrors(data.errors);
        }
      });
  };

  if (!dish) return <div>Loading...</div>;
  return (
    <div id="postReviewContainer">
      <div className="postReviewHeading">How was your meal?</div>
      <div className="post-review-errors">
        {errors.comment && errors.comment ? <>{errors.comment}</> : <div className="empty-space"> </div>}
      </div>
      <label>
        <input
          type="text"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          className="comment-input"
          placeholder="Leave your review here..."
        />
      </label>
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
        Submit Your Review
      </button>
    </div>
  );
}

export default CreateReviewModal;
