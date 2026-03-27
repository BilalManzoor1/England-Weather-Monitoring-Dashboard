# England Weather Monitoring Dashboard

This project provides a Power BI dashboard that visualizes current weather data for major cities in England. The data is fetched dynamically using a Python script from the METEO API.

# Features
Fetches live weather data for multiple cities using a Python script.
Includes temperature, wind speed, and weather description.
Stores data in a CSV file (data/weather_data.csv) for use in Power BI.
Dynamic Power BI dashboard with visuals for weather metrics.

# Setup Instructions
Clone the repository
git clone https://github.com/YourUsername/England-Weather-Monitoring-Dashboard.git

# Run the Python script
python script/fetch_weather.py

This will generate/update data/weather_data.csv with current weather information.

# Open the Power BI dashboard
Open Dashboard/WeatherDashboard.pbix in Power BI.

The dashboard reads data from the CSV file to create visuals.

# Notes
The Weather Description column in the CSV contains a text description (e.g., “Clear sky”, “Light rain”).

Wind speed is in km/h by default.

The .gitignore is set to ignore generated CSV to keep the repository clean.

# License
This project is open-source and free to use.
