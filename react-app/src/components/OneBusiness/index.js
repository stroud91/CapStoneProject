import React, { useEffect,useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchOneBusiness} from "../../store/business";
import {getDishesForBusiness} from "../../store/dish"
import { useParams, useHistory } from "react-router-dom";
import { deleteBusiness } from "../../store/business";
import { addItemToCart } from "../../store/cart";
import { fetchSingleBusinessReviews } from "../../store/review";
import {removeDishForBusiness} from '../../store/dish'
import DishCreationForm from '../CreateDishForm'
import "./OneBusiness.css";
import plusImage from '../../images/plusimage.jpg'


function BusinessDetails() {

    const history = useHistory();
    const dispatch = useDispatch();
    const { id } = useParams();

    const [loading, setLoading] = useState(true);
    const [showAddDishForm, setShowAddDishForm] = useState(false);

    const selectedBusiness = useSelector((state) => state.business.selectedBusiness);
    const dishes = useSelector((state) => state.dish.dishesForBusiness);
    const currentUser = useSelector((state) => state.session.user);
    const reviews = useSelector((state) => state.review.allReviews);
    const user = currentUser;



    const showAddDishFormFunction = () => {
        setShowAddDishForm(true);
    }

    const setSelectedDish = (id) => {
        history.push(`/dish/${id}`);
    }

        const handleEdit = (id) => {
            history.push(`/update-dish/${id}`);
        }

        const handleDelete = (id) => {

            dispatch(removeDishForBusiness(id));
        }

        const handleAddToCart = (dishId) => {

            dispatch(addItemToCart(dishId));
        }

    useEffect(() => {
        async function fetchData() {
            await dispatch(fetchOneBusiness(id));
            await dispatch(getDishesForBusiness(id));
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

            <div className="dishes-container">
                {dishes.map(dish => (
                    <div className="dish" onClick={() => setSelectedDish(dish.id)}>
                        <div className="dish-photo-container">
                            <img src={dish.image_id} alt={dish.name} className="dish-image" />
                        </div>
                        <div className="dish-info">
                        <h4>{dish.name}</h4>
                        <h4>Price: ${dish.price}</h4>
                        </div>
                        {user && selectedBusiness.owner_id === user.id && (
                            <div className="dish-owner-actions">
                                <button className="edit-btn" onClick={() => handleEdit(dish.id)}>Edit</button>
                                <button className="delete-btn" onClick={() => handleDelete(dish.id)}>Delete</button>
                            </div>
                        )}
                        {user && (
                        <div className="dish-user-actions">
                            <button className="add-cart-btn" onClick={() => handleAddToCart(dish.id)}>Add to Cart</button>
                        </div>
                        )}
                    </div>
                ))}
                {user && selectedBusiness.owner_id === user.id && (
                    <div className="add-new-dish" onClick={showAddDishFormFunction}>
                    <div className="add-dish-plus- container">
                            <img src={plusImage} alt=""className="plus-image" />
                        </div>
                 <p>Add a new dish</p>
                </div>
                )}
                {/* Conditionally render the DishCreationForm */}
                {showAddDishForm && <DishCreationForm />}
            </div>
        </div>
    );
}


export default BusinessDetails;
