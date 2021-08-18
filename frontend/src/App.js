import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import GoDataGathering from "./GoDataGathering";

function App() {
  sessionStorage.clear();
  return (
    <div>
      <Router>
        <Route exact path="/">
          <GoDataGathering />
        </Route>
        <Route path="/godata">
          <GoDataGathering />
        </Route>
      </Router>
    </div>
  );
}

export default App;
