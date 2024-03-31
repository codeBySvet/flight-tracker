# Import module to create HTTP calls
import requests
import folium
from folium.plugins import MarkerCluster


# Define the bounding box coordinates for Europe
lamin = 15  # Minimum latitude
lomin = -160  # Minimum longitude
lamax = 70  # Maximum latitude
lomax = -50  # Maximum longitude

# Custom icon URL


# Load custom icon and cache it
custom_icon = folium.features.CustomIcon('/Users/svetlinnachev/Desktop/Flight app/fly1/icon.png', icon_size=(12, 12))

# Make HTTP request to the OpenSky API with the specified bounding box (this works)
# response = requests.get(f"https://opensky-network.org/api/states/all?lamin={lamin}&lomin={lomin}&lamax={lamax}&lomax={lomax}")
# Make HTTP request to the OpenSky API with the specified bounding box (this does not work)
response = requests.get(f"https://opensky-network.org/api/states/all")
data = response.json()

m = folium.Map(location=(50, 25), zoom_start=4.45, tiles="cartodbpositron")


if 'states' in data and data['states']:

    # Create a MarkerCluster layer
    marker_cluster = MarkerCluster().add_to(m)

    # Iterate over each flight object
    for x in data['states']:
        name = x[1]
        long = x[5]
        lat = x[6]

        if name is not None and lat is not None and long is not None:
            folium.CircleMarker(
                location=[lat, long],
                popup=name,
                radius=5,  # Customize radius as needed
                color='red',  # Customize color as needed
                fill=False,
                fill_color='red'  # Same as color for filled marker
            ).add_to(marker_cluster)
            print(f"Flight: {name}, Longitude: {long}, Latitude: {lat}")

else:
    # Display a message indicating no flight data is available
    folium.Marker(
        location=(50, 25),
        popup="No flight data available",
        icon=folium.Icon(color='blue')
    ).add_to(m)
    print("IN ELSE STATEMENT ----------------------------------------------------")

# add marker one by one on the map
m.save("footprint.html")

