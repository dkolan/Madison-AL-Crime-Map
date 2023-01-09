import React, { useState } from "react";
import useSwr from "swr";

import WelcomeModal from "./components/WelcomeModal";
import Picker from './components/Picker'
import Map from './components/Map'

import './App.css';
import "react-datepicker/dist/react-datepicker.css";

const fetcher = (...args) => fetch(...args).then(response => response.json());

function App() {
  // Welcome Modal state
  const [show, setShow] = useState(true);
  const handleClose = () => {
    setShow(false);
  };

  // API Logic
  const apiUrl = "http://localhost:8000/api/incidents";
  const {data, error} = useSwr(apiUrl, { fetcher });

  // Incident Filtering state
  const incidents = data && !error ? data : [];
  const [filteredIncidents, setFilteredIncidents] = useState([]);

  return (
    <>
      <WelcomeModal 
        show={show}
        handleClose={handleClose}
      />
      <div className="wrapper">
        <div className="datepicker">
          <Picker 
            incidents={incidents} 
            filteredIncidents={filteredIncidents}
            setFilteredIncidents={setFilteredIncidents}
          />
        </div>
        <Map filteredIncidents={filteredIncidents} />
      </div>
    </>
  );
}

export default App;
