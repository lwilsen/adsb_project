"""Importing these modules to get the environment variable KPLER token, 
and to use the requests module to access the KPLER api."""

import os
import requests

kpler_access_token = os.getenv("KPLER_TOKEN")

URL = "https://api-lng.kpler.com/v1/trades?size=5"

payload = {}
headers = {
    'Authorization': f"Basic {kpler_access_token}"
}

response = requests.request("GET", URL, headers=headers, data=payload)

print(response.text)
