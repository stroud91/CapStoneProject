import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link,NavLink } from 'react-router-dom';
import noImage from "../../images/no-image.png"
import * as businessActions from '../../store/business';
import OpenModalButton from "../OpenModalButton";
import { useHistory } from "react-router-dom";
import DeleteModal from "../DeleteBusinessModal/index"


function OwnedBusinesses() {
    const dispatch = useDispatch();
    const history = useHistory();
    const currentUser = useSelector(state => state.session.user);

    const businesses = useSelector(state => state.business.list);

    const user = currentUser;

    const handleEditBusiness = (id) => {
        history.push(`/update-business/${id}/`);
    }

    useEffect(() => {
        dispatch(businessActions.getAllBusinesses());
    }, [dispatch]);

    const ownedBusinesses = businesses.filter(
        business => business.owner_id === currentUser.id
    );


    if (ownedBusinesses.length === 0) {
        return <div>Currently you have no businesses created. Will you want to create one?
                <div>
                <NavLink exact to="/create-business" className="create-business-button">Create a business</NavLink>
                </div>
            </div>

    }



    return (


        <ul className='businessMain__grid'>
            {ownedBusinesses && ownedBusinesses.map((business) => (
                <li key={business.id} className='businessMain__item'>
                    <p className="businessMain_name">{business.name}</p>
                    <div className="businessMain__image">
                        <img src={business.logo_id}
                            className='busImg'
                            alt={business.name}
                            key={business.id}
                        />
                    </div>

                    <p>{business.address}, {business.city}, {business.state} {business.zip_code}</p>
                    <p>{business.phone}</p>

                    <Link to={`/business/${business.id}`}>View More</Link>

                     <div className="business-actions">
                    <button className="edit-button" onClick={() => handleEditBusiness(business.id)}>Edit</button>
                    <OpenModalButton
                      buttonText="Delete"

                      modalComponent={<DeleteModal bus_data={business} />}
                      id={"delete-business-button"}
                    />
                   </div>

                </li>
            ))}
        </ul>
       
    );
}

export default OwnedBusinesses;
