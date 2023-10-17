import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import MainPageView from "./components/MainPageView";
import OneBusiness from "./components/OneBusiness";
import OneDish from "./components/OneDish";
import UserOrder from "./components/UserOrder";
import CreateBusinessForm from "./components/CreateBusinessForm";
import CreateDishForm from "./components/CreateDishForm";
import UpdateBusinessForm from "./components/UpdateBusinessForm";
import UpdateDishForm from "./components/UpdateDishForm";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login">
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route exact path="/">
            <MainPageView />
          </Route>
          <Route path="/business/:id">
            <OneBusiness />
          </Route>
          <Route path="/dish/:id">
            <OneDish />
          </Route>
          <Route path="/orders">
            <UserOrder />
          </Route>
          <Route path="/create-business">
            <CreateBusinessForm />
          </Route>
          <Route path="/create-dish">
            <CreateDishForm />
          </Route>
          <Route path="/update-business/:id">
            <UpdateBusinessForm />
          </Route>
          <Route path="/update-dish/:id">
            <UpdateDishForm />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
