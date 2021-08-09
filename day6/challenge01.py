#!/usr/bin/python3

import requests
import json
import datetime

url = "http://api.open-notify.org/iss-now.json"

res_dict = requests.get(url).json()

datetime_time = datetime.datetime.fromtimestamp(res_dict["timestamp"])

print(f"""
CURRENT LOCATION OF THE ISS:
Timestamp: {datetime_time}
Lon: {res_dict["iss_position"]["longitude"]}
Lat: {res_dict["iss_position"]["latitude"]}

""")
