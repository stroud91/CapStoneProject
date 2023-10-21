import React from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { getAllBusinesses , deleteBusiness } from "../../store/business";
import "./DeleteBusinessModal.css";
import { useModal } from "../../context/Modal";

export default function DeleteModal({ bus_data }) {
  console.log("DeleteModal is rendered", bus_data.id);
  const id = bus_data.id
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    return dispatch(deleteBusiness(id)).then(() => {
      closeModal();
      dispatch(getAllBusinesses());
      history.push('/owned')
    });
  };

  return (
    <div className="deleteSpotContainer">
      <div className="deleteHeader">Confirm Delete</div>
      <div className="deleteText">Are you sure you want to delete this business?</div>
      <div>
        <button
          className="confirm-yes cursor"
          onClick={handleSubmit}
        >
          Yes (Delete Business)
        </button>
        <button
          className="cancel"
          onClick={((e) => {
            closeModal();
          })}
        >
          No (Keep Business)
        </button>
      </div>
    </div>
  )
}
