import React from 'react'
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";

const Map = ({ filteredIncidents }) => {
	return(
		<MapContainer center={[34.69926, -86.74833]} zoom={13} scrollWheelZoom={false}>
		  <TileLayer
			attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
			url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
		  />
		  {filteredIncidents.map((incident) => (
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
	)
}

export default Map;