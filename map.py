import requests
import json

# call the OSMR API
# Import the required library
from geopy.geocoders import Nominatim

# Initialize Nominatim API
# https://www.openstreetmap.org/#map=11/12.9607/80.1858

def locate(l1, l2):
    geolocator = Nominatim(user_agent="MyApp")
    location1 = geolocator.geocode(l1)
    location2 = geolocator.geocode(l2)

    lon_1 , lat_1 = location1.longitude , location1.latitude
    lon_2 , lat_2= location2.longitude , location2.latitude

    r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon_1},{lat_1};{lon_2},{lat_2}?overview=false""")
    routes = json.loads(r.content)
    route_1 = routes.get("routes")[0]

    return route_1["duration"]
# print(route_1)

# # google API url
# url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin_coor}&destination={destination_coor}&mode=driving&key={'AIzaSyCLX4zAkTs588i7ncbcRhhE5xUYR06VS3g'}"