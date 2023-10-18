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
    const [showAddBusinesshForm, setShowAddBusinessForm] = useState(false);
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

    const handleEditBusiness = (id) => {
        history.push(`/update-business/${id}`);
    }

    const handleDeleteBusiness = (id) => {
        dispatch(deleteBusiness(id));
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
        <div className="business-info-container">
    <div className="business-logo">
        <img src={selectedBusiness.logo_id} alt="Business Logo" />
    </div>
    <div className="business-name">
        {/* Name of the business */}
        {selectedBusiness.name}
    </div>
    <div className="business-details">

        <p>About: {selectedBusiness.about}</p>
        <p>Address: {selectedBusiness.address}, {selectedBusiness.city}</p>
        <p>Email: {selectedBusiness.email}</p>
        <p>Phone Number: {selectedBusiness.phone}</p>
    </div>
    {user && selectedBusiness.owner_id === user.id && (
    <div className="business-actions">
        <button className="edit-button" onClick={() => handleEditBusiness(selectedBusiness.id)}>Edit</button>
        <button className="delete-button" onClick={() => handleDeleteBusiness(selectedBusiness.id)}>Delete</button>
    </div>
    )}
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
