import requests
import json
import folium

# Fetch's the data from the ISS API (open notify)
response = requests.get("http://api.open-notify.org/iss-now.json")
data = json.loads(response.text)
lat = float(data["iss_position"]["latitude"])
lon = float(data["iss_position"]["longitude"])

# Create a map centered on the current ISS location
m = folium.Map(location=[lat, lon], zoom_start=3)

# Add a marker for the ISS location
folium.Marker([lat, lon]).add_to(m)

# Save the map as an HTML file
m.save("map.html")

# Open the map in your default browser
import webbrowser
webbrowser.open("map.html")