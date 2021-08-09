#!/usr/bin/python3

import requests
import json
import datetime
import reverse_geocoder as rg

url = "http://api.open-notify.org/iss-now.json"

res_dict = requests.get(url).json()

datetime_time = datetime.datetime.fromtimestamp(res_dict["timestamp"])

print(f"""
CURRENT LOCATION OF THE ISS:
Timestamp: {datetime_time}
Lon: {res_dict["iss_position"]["longitude"]}
Lat: {res_dict["iss_position"]["latitude"]}
City: {rg.search((res_dict["iss_position"]["longitude"], res_dict["iss_position"]["latitude"]))[0]["name"]}

""")
