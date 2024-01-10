import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';
import * as businessActions from '../../store/business';
import noImage from "../../images/no-image.png";
import './Business.css';

function getPrev(business) {
    if (business.logo_id) {
        const previewImage = business.logo_id
        return previewImage ? previewImage.image_url : noImage;
    }
    return noImage;
}

function BusinessCard({ business }) {
    return (
        <div className='businessMain__item'>
            <div className="businessMain__image">
                <img src={business.logo_id}
                     className='businessMain__image'
                     alt={business.name}
                     key={business.id} />
            </div>
            <p className="businessMain_name">{business.name}</p>
            <p>{business.address}, {business.city}, {business.state} {business.zip_code}</p>
            <p>{business.phone_number}</p>
            <Link to={`/business/${business.id}`}>View More</Link>
        </div>
    );
}

function BusinessMainPage() {
    const dispatch = useDispatch();
    const businesses = useSelector(state => state.business.list);

    useEffect(() => {
        dispatch(businessActions.getAllBusinesses());
    }, [dispatch]);

    return (
        <div className='businessMain__grid'>
            {businesses && businesses.map(business => (
                <BusinessCard key={business.id} business={business} />
            ))}
        </div>
    );
}

export default BusinessMainPage;
