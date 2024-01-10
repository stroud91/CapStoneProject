import React from 'react';
import { useDispatch } from 'react-redux';
import { removeDishForBusiness } from '../../store/dish';
import { useHistory } from "react-router-dom";
import { getDishesForBusiness } from '../../store/dish';
import { useModal } from "../../context/Modal";

function DeleteDishModal({ businessId, dishId }) {

  const dispatch = useDispatch();
  const history = useHistory();
  const { closeModal } = useModal();

  const handleDelete = async (e) => {

   e.preventDefault();
    return dispatch(removeDishForBusiness(businessId, dishId)).then(() => {
      closeModal();
      dispatch(getDishesForBusiness(businessId));
      history.push(`/business/${businessId}`);
    });
  };

  return (
    <div className="modal-container">
      <h2>Confirm Deletion</h2>
      <p>Are you sure you want to delete this dish?</p>
      <div className="modal-buttons">
        <button onClick={handleDelete}>Yes, Delete</button>
        <button className="cancel" onClick={((e) => {
          closeModal();
          })}>Cancel</button>
      </div>
    </div>
  );
}

export default DeleteDishModal;
