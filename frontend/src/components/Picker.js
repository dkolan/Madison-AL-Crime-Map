import React, { useState, useEffect } from "react";
import DatePicker from "react-datepicker";

const isDateBetween = (minDate, maxDate, target) => {
	minDate.setHours(0,0,0,0)
	maxDate.setHours(0,0,0,0)
	target.setHours(0,0,0,0)
	return target.getTime() >= minDate.getTime() && target.getTime() <= maxDate.getTime();
}

const Picker = ({incidents, setFilteredIncidents}) => {
	const fourWeeksAgo = 24192e5
	const twoWeeksAgo = 12096e5
	const [startDate, setStartDate] = useState(Date.now() - fourWeeksAgo);
	const [endDate, setEndDate] = useState(Date.now() - twoWeeksAgo);

	useEffect(() => {
		handleDateChange();
	}, []);

	useEffect(() => {
			handleDateChange();
		}, [startDate, endDate]);

	const handleDateChange = () => {
		const newFilteredIncidents = [];
		const minDate = new Date(startDate)
		const maxDate = new Date(endDate)
		for (const i of incidents) {
			const date = new Date(i.datetime);
			if (isDateBetween(minDate, maxDate, date)) newFilteredIncidents.push(i);
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