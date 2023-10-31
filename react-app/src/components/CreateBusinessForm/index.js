import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import * as businessActions from '../../store/business';
import './CreateBusinessForm.css';

const CreateBusinessForm = () => {
    const dispatch = useDispatch();
    const history = useHistory();

    const [name, setName] = useState('');
    const [address, setAddress] = useState('');
    const [city, setCity] = useState('');
    const [state, setState] = useState('');
    const [zip_code, setZipCode] = useState('');
    const [phone_number, setPhoneNumber] = useState('');
    const [about, setAbout] = useState('');
    const [type, setType] = useState('');
    const [email, setEmail] = useState('');
    const [logo_id, setLogoId] = useState('');

    const [validationErrors, setValidationErrors] = useState([]);
    const [errors, setErrors] = useState([]);


    const currentUser = useSelector(state => state.session.user);
    const owner_id = currentUser ? currentUser.id : null;

    const validate = () => {
        const errors ={};

        if (!name || name.length < 5 || name.length > 50)  {
            errors.name="Business name must be between 5 and 50 characters.";
        }

        if (!address || address.length > 255) {
            errors.address="Invalid address.";
        }

        if (!city || city.length > 50) {
            errors.city="Invalid city.";
        }

        if (!state || state.length != 2) {
            errors.state="Invalid state.";
        }

        if (!zip_code || !/^\d{5}$/.test(zip_code)) {
            errors.zip_code="Invalid ZIP Code.";
        }

        if (!phone_number || !/^\d{10}$/.test(phone_number)) {
            errors.phone_number="Invalid phone number.";
        }

        if (!about || about.length > 500) {
            errors.about="Invalid about text.";
        }

        if (!type || type.length > 255) {
            errors.type="Invalid type.";
        }


        if (!email || !/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/.test(email)) {
            errors.email="Invalid email.";
        }


        if (!logo_id) {
            errors.logo_id="Logo ID is required.";
        }


        if (!owner_id) {
            errors.owner_id="Owner ID is required.";
        }

        return errors;
    };


    const handleSubmit = async (e) => {
        e.preventDefault();

        const errors = validate();

        if (Object.keys(errors).length > 0) {
            setValidationErrors(errors);
            return;
        }

        const DataBusiness = {
            name,
            address,
            city,
            state,
            zip_code,
            phone_number,
            about,
            type,
            email,
            logo_id,
            owner_id
        };
        await dispatch(businessActions.createNewBusiness(DataBusiness));

        history.push(`/owned`);


    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Name:
                    {validationErrors.name && <div className="error">{validationErrors.name}</div>}
                    <input type="text" value={name} onChange={e => setName(e.target.value)} />
                </label>
                <label>
                    Address:
                    {validationErrors.address && <div className="error">{validationErrors.address}</div>}
                    <input type="text" value={address} onChange={e => setAddress(e.target.value)} />
                </label>
                <label>
                    City:
                    {validationErrors.city && <div className="error">{validationErrors.city}</div>}
                    <input type="text" value={city} onChange={e => setCity(e.target.value)} />
                </label>
                <label>
                    State:
                    {validationErrors.state && <div className="error">{validationErrors.state}</div>}
                    <input type="text" value={state} onChange={e => setState(e.target.value)} />
                </label>
                <label>
                    Zip Code:
                    {validationErrors.zip_code && <div className="error">{validationErrors.zip_code}</div>}
                    <input type="text" value={zip_code} onChange={e => setZipCode(e.target.value)} />
                </label>
                <label>
                    Phone Number:
                    {validationErrors.phone_number && <div className="error">{validationErrors.phone_number}</div>}
                    <input type="text" value={phone_number} onChange={e => setPhoneNumber(e.target.value)} />
                </label>
                <label>
                    About:
                    {validationErrors.about && <div className="error">{validationErrors.about}</div>}
                    <textarea value={about} onChange={e => setAbout(e.target.value)} />
                </label>
                <label>
                    Type:
                    {validationErrors.type && <div className="error">{validationErrors.type}</div>}
                    <input type="text" value={type} onChange={e => setType(e.target.value)} />
                </label>
                <label>
                    Email:
                    {validationErrors.email && <div className="error">{validationErrors.email}</div>}
                    <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
                </label>
                <label>
                    Logo ID:
                    {validationErrors.logo_id && <div className="error">{validationErrors.logo_id}</div>}
                    <input type="text" value={logo_id} onChange={e => setLogoId(e.target.value)} />
                </label>
                <button type="submit">Create Business</button>
            </form>
        </div>
    );
};

export default CreateBusinessForm;
