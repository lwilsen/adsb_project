"""Importing these modules to get the environment variable KPLER token, 
and to use the requests module to access the KPLER api."""

import os
import requests
import requests.api

kpler_access_token = os.getenv("KPLER_TOKEN")

URL = "https://api-lng.kpler.com/v1/trades?size=5"

payload = {}
headers = {"Authorization": f"Basic {kpler_access_token}"}

response = requests.api.get(URL, headers=headers, data=payload, timeout=10)

print(response.text)
