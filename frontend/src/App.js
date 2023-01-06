import React, { useState } from "react";
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import useSwr from "swr";
import './App.css';

const fetcher = (...args) => fetch(...args).then(response => response.json());

function App() {
  const apiUrl = "http://localhost:8000/api/incidents";
  const {data, error} = useSwr(apiUrl, { fetcher });

  const incidents = data && !error ? data : [];

  const [show, setShow] = useState(true);

  const handleClose = () => setShow(false);

  return (
    <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Madison, AL Criminal Incident Map</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>
            Welcome! This is a proof of concept on plotting crime incidents published by the&nbsp;
            <a href="https://www.madisonal.gov/219/Police">Madison City Police</a>.
            The data was provided by the <a href="https://www.madisonal.gov/Archive.aspx">Madison City Archive Center</a> as a PDF, parsed, and added to a RESTful API.
          </p>
          <p>
            Unfortunately, the city chooses to present these reports in a format (PDF) which is not conducive to fair and open governmental practices. Please urge your&nbsp;
            <a href="https://www.madisonal.gov/1195/Madison-Police-Citizens-Advisory-Committ">Police Citizens Advisory Committee</a> representative to implement IT practices
            that allow for citizens to have fair and open access to this public data.
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
        {incidents.map((incident) => (
          <Marker
            key = {incident.id}
            position = {[
              incident.latitude,
              incident.longitude
            ]}
            >
              <Popup>
                <h5>{incident.location}</h5>
                <p>{incident.caseNumber}</p>
                <p>{new Date(incident.datetime).toLocaleDateString('en-US')} @ {new Date(incident.datetime).toLocaleTimeString('en-US')}</p>
                <p>{incident.description}</p>
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </>
  );
}

export default App;
