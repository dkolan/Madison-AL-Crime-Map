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
  // const {data, error} = useSwr(apiUrl, { fetcher });
  const {data, error} = useSwr(apiUrl, async (url) => {
    const response = await fetch(url);
    return response.json();
  }, { suspense: true });  

  // Incident Filtering state
  const incidents = data && !error ? data : [];
  console.log(incidents)
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
            setFilteredIncidents={setFilteredIncidents}
          />
        </div>
        <Map filteredIncidents={filteredIncidents} />
      </div>
    </>
  );
}

export default App;
