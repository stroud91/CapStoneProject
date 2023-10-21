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
        const errors = [];

        if (!name || name.length < 5 || name.length > 50)  {
            errors.push("Business name must be between 5 and 50 characters.");
        }

        if (!address || address.length > 255) {
            errors.push("Invalid address.");
        }

        if (!city || city.length > 50) {
            errors.push("Invalid city.");
        }

        if (!state || state.length != 2) {
            errors.push("Invalid state.");
        }

        if (!zip_code || !/^\d{5}$/.test(zip_code)) {
            errors.push("Invalid ZIP Code.");
        }

        if (!phone_number || !/^\d{10}$/.test(phone_number)) {
            errors.push("Invalid phone number.");
        }

        if (!about || about.length > 500) {
            errors.push("Invalid about text.");
        }

        if (!type || type.length > 255) {
            errors.push("Invalid type.");
        }


        if (!email || !/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/.test(email)) {
            errors.push("Invalid email.");
        }


        if (!logo_id) {
            errors.push("Logo ID is required.");
        }


        if (!owner_id) {
            errors.push("Owner ID is required.");
        }

        return errors;
    };


    const handleSubmit = async (e) => {
        e.preventDefault();

        const errors = validate();

        if (errors.length > 0) return setValidationErrors(errors);

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
                    <input type="text" value={name} onChange={e => setName(e.target.value)} />
                </label>
                <label>
                    Address:
                    <input type="text" value={address} onChange={e => setAddress(e.target.value)} />
                </label>
                <label>
                    City:
                    <input type="text" value={city} onChange={e => setCity(e.target.value)} />
                </label>
                <label>
                    State:
                    <input type="text" value={state} onChange={e => setState(e.target.value)} />
                </label>
                <label>
                    Zip Code:
                    <input type="text" value={zip_code} onChange={e => setZipCode(e.target.value)} />
                </label>
                <label>
                    Phone Number:
                    <input type="text" value={phone_number} onChange={e => setPhoneNumber(e.target.value)} />
                </label>
                <label>
                    About:
                    <textarea value={about} onChange={e => setAbout(e.target.value)} />
                </label>
                <label>
                    Type:
                    <input type="text" value={type} onChange={e => setType(e.target.value)} />
                </label>
                <label>
                    Email:
                    <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
                </label>
                <label>
                    Logo ID:
                    <input type="text" value={logo_id} onChange={e => setLogoId(e.target.value)} />
                </label>
                <button type="submit">Create Business</button>
            </form>
            {errors.length > 0 && (
                <div>
                    {errors.map((error, idx) => (
                        <div key={idx} className="error">
                            {error}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default CreateBusinessForm;
