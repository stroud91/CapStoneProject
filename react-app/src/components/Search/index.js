import React, { useState } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useSelector, } from "react-redux";
import { useDispatch } from "react-redux";
import { searchBusinessByName } from "../../store/business";
import "./Search.css";
import { NavLink } from "react-router-dom/cjs/react-router-dom";

function SearchBar() {
  const dispatch = useDispatch();
  const history = useHistory();
  const [searchTerm, setSearchTerm] = useState('');
  const [searched, setSearched] = useState(false)
  const query = useSelector(state => state.business.search)
  console.log('query', query)
  const handleChange = (e) => {
    setSearchTerm(e.target.value)
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (searchTerm !== '') {
      await dispatch(searchBusinessByName(searchTerm));
      setSearched(true);
      history.push('/search');
    } else {
      history.push('/all')
    }
  };

  const handleReturn = async (e) => {
    e.preventDefault();
    history.push("/")
  };

  const setSelectedDish = (id,event) => {
    event.stopPropagation();
    history.push(`/dish/${id}`);
}

  return (
    <section className='main-search-section'>
        <div className='search-info'>
            <form className='main-search-form' onSubmit={handleSubmit}>
                <input
                    className='main-search-input'
                    name="search"
                    type="text"
                    placeholder="Search for your next dining experience"
                    value={searchTerm}
                    onChange={handleChange}
                />
                <button className='search-button' type='submit'>
                    <i className="fas fa-search"></i>
                </button>
            </form>
        </div>
        <div>

        </div>
        {/* Display Queried Businesses and Dishes */}
        <div className="dish-listings">
    {query && query.queried_dishes && query.queried_dishes.map((dish, idx) => (
        <div key={idx} className="dish-item">
           <NavLink to={`/dish/${dish.id}`} onClick={(e) => setSelectedDish(dish.id, e)}></NavLink>
          <div>
            <img src={dish.dish_image} alt="" />
          </div>
          <div>
            <h2>Dish: {dish.name}</h2>
            <p>Price: {dish.price}</p>
            <p>Category: {dish.category_name}</p>
            <p>From: {dish.business_name}</p></div>

        </div>
        
    ))}
</div>
    </section>
)
}

export default SearchBar;
