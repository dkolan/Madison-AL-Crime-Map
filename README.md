# Madison, AL Crime Map
This is another "sprint" project I put together during my Winter Break between my Fall 2022 and Spring 2023 semesters. The genesis of this project was due to Catherine and I moving back to her hometown of Madison, AL so I could begin my co-op terms at Adtran and we could be close to her family. Naturally, when looking for a place to live, my mom got duped by one of the many alarmist crime map websites that seem to show everywhere in scary shades of red. Upon learning that the City of Madison publishes bi-weekly reports with all crime "incidents" logged by the police as PDFs likely created in Microsoft Word, I decided there must be a better solution. My goal is to encourage my local government to publish their data in a more accessible way, so that citizens can be empowered to explore that data and create new tools like this.

Because I would be working primarily in Python on my co-op team at Adtran, I decided to create a REST API using Django for the backend to store the crime incident data. Currently there is limited automation grabbing the PDFs from Madison, as they've recently changed the from a key:value format to a table format that does not play nice with Tabula and Pandas. Data is parsed using the Nominatim (OpenStreetMap) geocoding API with Google Maps as a paid fallback (primarily when addresses are only listed as cross-streets). Better automation involving downloading newly published files (Celery) and PDF parsing (Tabula or OCR) is planned for the future. Unit tests are written utilizing Django's built-in unit testing functionality.

The front-end is written in React, primarily utilzing Leaflet to render the map and markers. Filtering by dates is accomplished by getting imput from React Date Picker.

# Todo
0. Render one marker if incident details share the same Case Number and/or Location to prevent overlapping.
1. Implement marker clustering for markers that are located closely together.
2. Write Integration tests, especially for the custom Admin upload for uploading new data.
3. Deploy
4. CI/CD testing so I can ensure new builds don't break anything and can be deployed safely.
5. Automate the parsing of PDF report from the city.

# Demo
![]()
