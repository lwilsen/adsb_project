import requests
import os
import time
from datetime import datetime, timezone
import pandas as pd
import schedule

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

API_HOST = "adsbexchange-com1.p.rapidapi.com"

URL_TEMP = "https://{HOST}/v2/lat/{LAT}/lon/{LONG}/dist/{DIST}/"

headers = {
    "x-rapidapi-key":RAPID_API_KEY,
    "x-rapidapi-host":API_HOST
}

# Define area of interest

LATITUDE = 27.842490
LONGITUDE = -82.503222
DISTANCE = 50

#initialize database to get data

DATA_DIR = "adsb_data"
os.makedirs(DATA_DIR, exist_ok=True) #creates new directory if needed, otherwise does nothing

#Initialize databse for data with differing number of columns, (or that doesn't fit with focus features)
BAD_DATA_DIR = "adsb_data/weird_data"
os.makedirs(BAD_DATA_DIR, exist_ok=True)

#create a function to get and store data

def get_n_store():
    """Construct API call"""
    api_url = URL_TEMP.format(HOST = API_HOST, LAT = LATITUDE, LONG = LONGITUDE, DIST = DISTANCE)

    headers = {
        "x-rapidapi-key":RAPID_API_KEY,
        "x-rapidapi-hooost":API_HOST
    }

    focus_features = ['hex', 'flight', 't', 'category', 'alt_baro', 'alt_geom', 'gs',
       'track', 'baro_rate','geom_rate', 'emergency', 'lat', 'lon',
       'nac_p', 'nac_v','alert','seen', 'nav_altitude_mcp',
       'nav_heading', 'true_heading']

    try:
        response = requests.get(api_url,headers=headers)
        #Parse response
        adsb_data = response.json().get("ac",[])

        if not adsb_data:
            return(f"{datetime.now(timezone.utc)}: No data returned.")
        """Try to get only the features we're interested in, and make sure that 
        there are a correct number of columns."""
        
        try:
            df = pd.DataFrame(adsb_data).loc[:, focus_features]
            bad_data_path = os.path.join(BAD_DATA_DIR, "bad_data.csv")
            
            if (df.columns != focus_features).any():
                #Don't want to waste an api call on data that's missing a column or two
                df_weird = pd.DataFrame(adsb_data)
                df_weird['timestamp'] = datetime.now(timezone.utc)

                if not os.path.isfile(bad_data_path):
                    df_weird.to_csv(bad_data_path, index=False, mode="w",header=True)
                else:
                    df_weird.to_csv(bad_data_path, index=False, mode="a", header=False)

        except Exception as e:
            print(f"Feature selection error: {e}")

        if not df.shape[1] == 20:
            return("df.shape[1] != 20")
        
        df['timestamp'] = datetime.now(timezone.utc)
        df['mph'] = (df['gs'] * 1.151)

        file_path = os.path.join(DATA_DIR, "adsb_data.csv")

        if not os.path.isfile(file_path):
            df.to_csv(file_path, index=False, mode="w",header=True)
        else:
            df.to_csv(file_path, index=False, mode="a", header=False)

        print(f"{datetime.now(timezone.utc)}: Data fetched and stored!")


    except Exception as e:
        #returns the error with the time it occurred
        return(f'{datetime.now(timezone.utc)}: An error occured: ({e})')

'''Schedule function to run every 5 minutes (equates to 288 calls/24hr)'''

schedule.every(5).minutes.do(get_n_store)

print(f"{datetime.now(timezone.utc)}: Getting Data!")

while True:
    schedule.run_pending()
    time.sleep(1)