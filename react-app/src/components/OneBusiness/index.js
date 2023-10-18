import React, { useEffect,useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchOneBusiness} from "../../store/business";
import {setDishesForBusiness} from "../../store/dish"
import { useParams, useHistory } from "react-router-dom";
import { deleteBusiness } from "../../store/business";
import { fetchSingleBusinessReviews } from "../../store/review";
import "./OneBusiness.css";

function BusinessDetails() {
    const history = useHistory();
    const dispatch = useDispatch();
    const { id } = useParams();
    const [loading, setLoading] = useState(true);
    const [selectedDish, setSelectedDish] = useState(null);
    const selectedBusiness = useSelector((state) => state.business.selectedBusiness);
    const dishes = useSelector((state) => state.business.dishes);
    const currentUser = useSelector((state) => state.session.user);
    const reviews = useSelector((state) => state.review.allReviews);
    const user = currentUser;




    useEffect(() => {
        async function fetchData() {
            await dispatch(fetchOneBusiness(id));
            await dispatch(setDishesForBusiness(id));
            await dispatch(fetchSingleBusinessReviews(id));
            setLoading(false);
        }
        fetchData();
    }, [dispatch, id]);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div className="business-container">
            {/* Display Selected Business Information */}
            <h2>{selectedBusiness.name}</h2>
            <p>{selectedBusiness.address}</p>
            <p>{selectedBusiness.description}</p>
            {/* ... other business information ... */}

            {/* Display the list of dishes */}
            <h3>Dishes:</h3>
            <ul>
                {selectedBusiness.dishes.map(dish => (
                    <li key={dish.id}>
                        <button onClick={() => setSelectedDish(dish)}>{dish.name}</button>
                    </li>
                ))}
            </ul>

            {/* If a dish is selected, display its details and reviews */}
            {selectedDish && (
                <div className="selected-dish">
                    <h4>{selectedDish.name}</h4>
                    <img src={selectedDish.image_id} alt={selectedDish.name} />
                    <p>{selectedDish.description}</p>
                    <p>Price: ${selectedDish.price}</p>
                    <h5>Reviews:</h5>
                    <ul>
                        {selectedDish.reviews.map((review, index) => (
                            <li key={index}>
                                <p>{review.comment}</p>
                                {/* ... other review details ... */}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default BusinessDetails;
