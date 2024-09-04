import os
import requests

kpler_access_token = os.getenv("KPLER_TOKEN")

url = "https://api-lng.kpler.com/v1/trades?size=5"

payload = {}
headers = {
    'Authorization': f"Basic {kpler_access_token}"
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)