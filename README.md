# Madison, AL Crime Map
This is a full stack web application meant to accept data published by the Madison City Police Department](https://www.madisonal.gov/Archive.aspx?AMID=67), and render it based off the geocoded latitude and longitude generated by calls to the Nominatim (OpenStreetMaps) or Google Maps geocoding APIs. 

The backend is powered by a PostgreSQL database with Django serving up the information via a REST API. Data is primarily added in bulk by uploading a CSV file generated by some scripts I have developed for parsing the MCPD PDFs. This was also intended to be consumable by the public for anyone that desired to utilize it for other applications such as analyzing the data. My hope is that my local government may see the benefit in publishing data in this open and fair way.

The front end is powered by React, utizling the react-leaflet and Leaflet libraries for the mapping. The data is consumed via the API and then can be filtered by date. I hope to add more options for filtering, visualizing, and exporting data in the future.

I initially wanted to do this project prior to my first term at Adtran, in order to learn more about Docker. To that end, the project can be ran locally utilizing `docker compose up`. I also hope to improve upon my tools for parsing the data, as the current format of the PDFs does not lend itself to libraries like Tabula or pdfplumber. I will add sample data to the resources folder.

## To Run
1. Have docker/docker daemon running locally
2. Run `docker compose up -d --build` in the root folder of the project.
3. To add data to the DB, you can use the test data located in: `./resources/test_data_december_2022.csv`
4. Navigate to `http://localhost:8000/admin/apis/incident/upload-csv/` and upload the CSV data.
5. API is available at: `http://localhost:8000/api/incidents` and Map is available at: `http://localhost:3000/`

# Background 
My well-intentioned mom got misled by one of the many alarmist crime map websites that seem to show everywhere in scary shades of red. Upon learning that the City of Madison publishes bi-weekly reports with all crime "incidents" logged by the police as PDFs likely created in Microsoft Word, I decided there must be a better solution. My goal is to present this data in an objective way and for this to serve as a proof of concept for my local government about how they can and should publish data in an open and secure way.

# Todo
0. Refactor to add more error handling and cleanliness, especially to handle edge cases of text/spreadsheet editors automatically formatting data.
1. Render one marker if incident details share the same Case Number and/or Location to prevent overlapping.
2. Implement marker clustering for markers that are located closely together.
3. Write Integration tests, especially for the custom Admin upload for uploading new data.
4. Deploy
5. CI/CD testing so I can ensure new builds don't break anything and can be deployed safely.
6. Automate the parsing of PDF report from the city.

# Demo
![](https://github.com/dkolan/Madison-AL-Crime-Map/blob/main/resources/crimemap.gif)
