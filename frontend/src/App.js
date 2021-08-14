import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";
// import Error from "./layout/Error";
import TopBar from "./topbar";
import BasePage from "./BasePage";
// import SignIn from "./authentication/signin";
// import SignUp from "./authentication/signup";
// import { useAuth } from "./authentication/auth";


function App() {
  sessionStorage.clear();
  // const [loggedIn] = useAuth();
  // if (loggedIn) {
    return (
      <div>
        <Router>
        <TopBar/>
          <BasePage>
          
            {/* <Switch>
              <Route
                exact
                path="/"
                render={() => {
                  return loggedIn ? (
                    <Redirect to="/taskboard" />
                  ) : (
                    <Redirect to="/login" />
                  );
                }}
              />
              <Route path="*">
                <Error />
              </Route>
            </Switch>
          </BasePage>
        </Router>
      </div>
    );
  } else {
    return (
      <div className="container">
        <Router>
          <Switch>
            <Route
              exact
              path="/"
              render={() => {
                return loggedIn ? (
                  <Redirect to="/taskboard" />
                ) : (
                  <Redirect to="/login" />
                );
              }}
            />
            <Route exact path="/login">
              <SignIn />
            </Route>
            <Route path="/signup">
              <SignUp />
            </Route>
            <Route path="*">
              <Error />
            </Route>
          </Switch> */}
          </BasePage>
        </Router>
      </div>
    );
  {/* } */}
}

export default App;
