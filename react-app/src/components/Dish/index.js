import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import OpenModalButton from "../OpenModalButton";
import DeleteModal from "../DeleteDishModal";
import EditDishModal from "../EditDishModal";
function DishInfo({ dish }) {
    const dispatch = useDispatch();
    const currentUser = useSelector(state => state.session.user);

    const handleDelete = (dishId) => {
        
    };

    return (
        <div className="dish-info-container">
            <Link to={`/dish/${dish.id}`} className="dish-link">
                <img src={dish.image_id} alt={dish.name} className="dish-image" />
                <h3>{dish.name}</h3>
                <p>{dish.description}</p>
                <span>${dish.price.toFixed(2)}</span>
            </Link>

            {currentUser && currentUser.id === dish.business_id && (
                <div className="dish-buttons">
                    <OpenModalButton
                        buttonText="Edit"
                        modalComponent={<EditDishModal dish={dish} />}
                        id={`dish-edit-button-${dish.id}`}
                    />
                    <OpenModalButton
                        buttonText="Delete"
                        modalComponent={<DeleteModal id={dish.id} onDelete={() => handleDelete(dish.id)} />}
                        id={`dish-delete-button-${dish.id}`}
                    />
                </div>
            )}
        </div>
    );
}

export default DishInfo;
