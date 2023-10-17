import React, { useState, useEffect } from "react";
import Search from "../Search";
import yelgImg from "../../images/dc.png";
import './MainPageView.css';

function MainPage() {
  const [search, setSearch] = useState('');
  const [businesses, setBusinesses] = useState([]);
  const [topRatedDishes, setTopRatedDishes] = useState([]);
  const [topOrderedDishes, setTopOrderedDishes] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    
  }

  const handleChange = (e) => {
    setSearch(e.target.value);
  }

  useEffect(() => {
    async function fetchData() {
      const businessesResponse = await fetch("/api/business/");
      const businessesData = await businessesResponse.json();
      setBusinesses(businessesData);

      const topRatedResponse = await fetch("/api/dish/top-rated");
      const topRatedData = await topRatedResponse.json();
      setTopRatedDishes(topRatedData);

      const topOrderedResponse = await fetch("/api/dish/top-ordered");
      const topOrderedData = await topOrderedResponse.json();
      setTopOrderedDishes(topOrderedData);
    }

    fetchData();
  }, []);

  return businesses.length > 0 ? (
    <div className='main-page-container'>
      <header className='main-header'>
        <Search handleSubmit={handleSubmit} handleChange={handleChange} search={search} />
      </header>

      <div className="main-page-image-container">
        <img src={yelgImg} alt="Cover" />
        <div className="image-text">Discover your new favorite restaurant</div>
      </div>

      <section className="top-rated-dish">
        <h2>Top Rated Dish</h2>
        <div className="dish-container">
          {topRatedDishes.map(dish => (
            <div key={dish.id} className="dish-card">
              <p>{dish.name}</p>
              <p>{dish.rating} ★</p>
            </div>
          ))}
        </div>
      </section>

      <section className="top-ordered-dish">
        <h2>Top Ordered Dish</h2>
        <div className="dish-container">
          {topOrderedDishes.map(dish => (
            <div key={dish.id} className="dish-card">
              <p>{dish.name}</p>
              <p>{dish.orders}</p>
            </div>
          ))}
        </div>
       </section>

      <footer className='main-footer'>
        <p>&copy; 2023 Capstone Project - Developed by Ledian Fekaj - React - Python - Flask - SQLAlchemy - PostgreSQL - Redux</p>
      </footer>
    </div>
  ) : (
    <div>Loading...</div>
  );
}

export default MainPage;
