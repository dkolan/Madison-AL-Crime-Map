import React, { useState } from "react";
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import { Icon } from "leaflet";
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import useSwr from "swr";
import './App.css';

const fetcher = (...args) => fetch(...args).then(response => response.json());

function App() {
  const apiUrl = "http://localhost:8000/api/incidents";
  const {data, error} = useSwr(apiUrl, { fetcher });

  const incidents = data && !error ? data : [];
  console.log(incidents)

  const [show, setShow] = useState(true);

  const handleClose = () => setShow(false);

  return (
    <>
       <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Madison, AL Crime Map</Modal.Title>
        </Modal.Header>
          <Modal.Body>
            <p>
              Welcome! This is a proof of concept on plotting crime incidents published by the
              <a href="https://www.madisonal.gov/219/Police"> Madison City Police</a>.
              The data was provided by the <a href="https://www.madisonal.gov/Archive.aspx">Madison City Archive Center</a> as a PDF, parsed, and added to a RESTful API.
            </p>
            <p>
              Unfortunately, as of 7/22/2022, they have removed the PDF incident reports and there is no recent data to import. Please stay tuned for future updates when Madison City
              implements their new service.
            </p>
            <p>
              This data is from: 4/22/2022 to 4/28/2022.
            </p>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
              Close
            </Button>
          </Modal.Footer>
      </Modal>
      <MapContainer center={[34.69926, -86.74833]} zoom={13} scrollWheelZoom={false}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
      </MapContainer>
    </>
  );
}

export default App;
