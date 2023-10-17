import React from 'react';
import { useDispatch } from 'react-redux';
import { removeDishForBusiness } from '../../store/dish';

function DeleteDishModal({ id, onDelete, businessId }) {
  const dispatch = useDispatch();

  const handleDelete = async () => {
    await dispatch(removeDishForBusiness(businessId, id));
    onDelete();
  };

  return (
    <div className="modal-container">
      <h2>Confirm Deletion</h2>
      <p>Are you sure you want to delete this dish?</p>
      <div className="modal-buttons">
        <button onClick={handleDelete}>Yes, Delete</button>
        <button onClick={onDelete}>Cancel</button>
      </div>
    </div>
  );
}

export default DeleteDishModal;
