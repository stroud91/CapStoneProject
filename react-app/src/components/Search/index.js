import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useSelector, } from "react-redux";
import { useDispatch } from "react-redux";
import { searchBusinessByName } from "../../store/business";
import "./Search.css";

function SearchBar() {
  const dispatch = useDispatch();
  const history = useHistory();
  const [searchTerm, setSearchTerm] = useState('');
  const [searched, setSearched] = useState(false)

  const handleChange = (e) => {
    setSearchTerm(e.target.value)
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (searchTerm !== '') {
      await dispatch(searchBusinessByName(searchTerm));
      setSearched(true);
      history.push('/business/search');
    }
  };
  useEffect(() => {
    dispatch(searchBusinessByName(searchTerm))
  }, [dispatch]);


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
          <i class="fas fa-search"></i>
          </button>
        </form>
      </div>
    </section>
  )
}
export default SearchBar;
