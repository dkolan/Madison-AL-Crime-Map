import React from "react";
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

const WelcomeModal = ({ show, handleClose }) => {
	return (
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
	);
};

export default WelcomeModal;