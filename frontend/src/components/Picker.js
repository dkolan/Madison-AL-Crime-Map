import React, { useState, useEffect } from "react";
import DatePicker from "react-datepicker";

const Picker = ({incidents, filteredIncidents, setFilteredIncidents}) => {
	const fourWeeksAgo = 24192e5
	const twoWeeksAgo = 12096e5
	const [startDate, setStartDate] = useState(Date.now() - fourWeeksAgo);
	const [endDate, setEndDate] = useState(Date.now() - twoWeeksAgo);

	useEffect(() => {
			handleDateChange();
		}, [startDate, endDate]);

	const handleDateChange = () => {
		const newFilteredIncidents = [];
		const minDate = new Date(startDate)
		const maxDate = new Date(endDate)
		for (const i of incidents) {
			const date = new Date(i.datetime);
			if (minDate.toLocaleDateString() <= date.toLocaleDateString() 
					&& maxDate.toLocaleDateString() >= date.toLocaleDateString()) {
				newFilteredIncidents.push(i);
			}
		}
		setFilteredIncidents(newFilteredIncidents);
	}

	return (
		<div className="date-picker-container">
			<p className="date-picker-label">Start Date</p>
			<DatePicker
				selected={startDate}
				onChange={(date) => {
					setStartDate(date);
				}}
				selectsStart
				startDate={startDate}
				endDate={endDate}
			/>
			<p className="date-picker-label">End Date</p>
			<DatePicker
				selected={endDate}
				onChange={(date) => {
					setEndDate(date);
				}}
				selectsEnd
				startDate={startDate}
				endDate={endDate}
				minDate={startDate}
			/>
		</div>
	);
};

export default Picker;