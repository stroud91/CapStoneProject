import React, { useEffect,useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import noImage from "../../images/no-image.png"
import { searchBusinessByName } from "../../store/business";
import { NavLink, useHistory} from "react-router-dom/cjs/react-router-dom";
function QueryBusiness() {
  const dispatch = useDispatch();
  const history = useHistory();
  const [searchTerm, setSearchTerm] = useState('');
  const [searched, setSearched] = useState(false)
  const query = useSelector(state => state.business.search)
  console.log('query', query)
  const handleChange = (e) => {
    setSearchTerm(e.target.value)
  };

  const setSelectedDish = (id,event) => {
    event.stopPropagation();
    history.push(`/dish/${id}`);
}

  return (
    <div>
        {/* Display Queried Businesses and Dishes */}
        <div className="dish-container">

    {query && query.queried_dishes && query.queried_dishes.map((dish, idx) => (
        <div key={idx} className="dish-card">
           <NavLink to={`/dish/${dish.id}`} onClick={(e) => setSelectedDish(dish.id, e)}></NavLink>
          <div>
            <img src={dish.dish_image} alt="" />
          </div>
          <div>
            <h2>Dish: {dish.dish_name}</h2>
            <p>Price: {dish.dish_price}</p>
            <p>From: {dish.business_name}</p></div>
        </div>

    ))}
</div>
    </div>
  );
}

export default QueryBusiness;
