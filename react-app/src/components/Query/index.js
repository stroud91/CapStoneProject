import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import noImage from "../../images/no-image.png"
import { searchBusinessByName } from "../../store/business";

function QueryBusiness() {
  const dispatch = useDispatch();
  let businesses = useSelector((state) => state.business.search);

  businesses = businesses["queried businesses"];
  console.log("This is the result of the search bar", businesses);

  useEffect(() => {
    dispatch(searchBusinessByName());
  }, [dispatch]);


  return (
    <div>
      {businesses.length === 0 ? (
        <div>
          <p> No restaurants found. Please try a different search.</p>
          <Link to="/">
            <button className="noResultButton">Go back to main page</button>
          </Link>
        </div>
      ) : (

        <ul className="businessMain__grid">
          {businesses &&
            businesses.map((business) => (
              <li key={business.id} className="businessMain__item">
                <div className="businessMain__image">
                  <img src={business.logo_id}
                    className='busImg'
                    alt={business.name}
                    key={business.id}
                  />
                </div>
                <p className="businessMain_name">{business.name}</p>
                <p>
                  {business.address}, {business.city}, {" "}
                  {business.zip_code}
                </p>
                <p>{business.phone_number}</p>
                <Link to={`/business/${business.id} `}>View More</Link>
              </li>
            ))}
        </ul>
      )}
    </div>
  );
}

export default QueryBusiness;
