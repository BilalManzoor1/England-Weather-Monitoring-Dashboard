import requests
import pandas as pd
import os

# Weather code mapping
weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Heavy rain showers",
    82: "Violent rain showers"
}

cities = {
    "London": (51.5072, -0.1276, "South"),
    "Manchester": (53.4808, -2.2426, "North"),
    "Birmingham": (52.4862, -1.8904, "Midlands"),
    "Leeds": (53.8008, -1.5491, "North"),
    "Brighton": (50.8225, -0.1372, "South"),
    "Liverpool": (53.4084, -2.9916, "North"),
    "Bristol": (51.4545, -2.5879, "South"),
    "Sheffield": (53.3811, -1.4701, "North"),
    "Newcastle": (54.9783, -1.6178, "North"),
    "Nottingham": (52.9548, -1.1581, "Midlands"),
    "Leicester": (52.6369, -1.1398, "Midlands"),
    "Southampton": (50.9097, -1.4044, "South"),
    "Portsmouth": (50.8198, -1.0880, "South"),
    "Oxford": (51.7520, -1.2577, "South"),
    "Cambridge": (52.2053, 0.1218, "South"),
    "Reading": (51.4543, -0.9781, "South"),
    "Derby": (52.9225, -1.4746, "Midlands"),
    "Coventry": (52.4068, -1.5197, "Midlands"),
    "Hull": (53.7457, -0.3367, "North"),
}

data = []

for city, (lat, lon, region) in cities.items():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url).json()
    
    weather = response.get("current_weather", {})
    code = weather.get("weathercode")

    data.append({
        "City": city,
        "Region": region,
        "Latitude": lat,
        "Longitude": lon,
        "Temperature": weather.get("temperature"),
        "Wind Speed": weather.get("windspeed"),
        "Weather Code": code,
        "Weather Description": weather_codes.get(code, "Unknown"),
        "Time": weather.get("time")
    })

df = pd.DataFrame(data)

# Save to data folder
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

data_folder = os.path.join(parent_dir, "data")
os.makedirs(data_folder, exist_ok=True)

output_path = os.path.join(data_folder, "weather_data.csv")

df.to_csv(output_path, index=False)

print(f"\nFile saved at: {output_path}")