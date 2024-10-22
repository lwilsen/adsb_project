import sqlite3
import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException, Request

'''SQLITE'''

def query_database(q):
    '''Queries sqlite databse for current adsb data'''

    try:
        conn = sqlite3.connect('/app/adsb_data.db')
        cursor = conn.cursor()
        cursor.execute(q)
        cols = [description[0] for description in cursor.description]
        data = cursor.fetchall()
        conn.close
        return {"Columns":cols, "Data": data}
    except sqlite3.Error as e:
        return {"Error": str(e)}
    
'''Unpickling models and encoder'''

with open("rf_best_mod.pkl",'rb') as mod:
    rf_mod = pickle.load(mod) 

with open("adsb_le.pkl", 'rb') as f:
    le = pickle.load(f)
'''Fast API'''

app = FastAPI()

@app.post("/predict-data")
async def predict(request : Request):

    try:
        cols = ['lon', 
        'emergency', 
        'flight', 
        'nac_p', 
        'gs', 
        't', 
        'alert', 
        'baro_rate',
        'alt_baro', 
        'track', 
        'hex', 
        'alt_geom', 
        'lat', 
        'geom_rate',
        'nav_altitude_mcp', 
        'nac_v']
    
        data = await request.json()

        

        df = pd.DataFrame([data], columns=cols)
        print(df)

        #predict
        prediction = rf_mod.predict(df)[0]

        mapping = {0: 'A0 : No ADS-B emitter category information.',
         1: 'A1 : Light (< 15500 lbs)',
         3: 'A2 : Small (15500 to 75000 lbs)',
         14: 'A3 : Large (75000 to 300000 lbs)',
         15: 'A4 :  High vortex large (aircraft such as B-757)',
         20: 'A5 : Heavy (> 300000 lbs)',
         16: 'A6 : High performance (> 5g acceleration and 400 kts)',
         10: 'A7 : Rotorcraft – Any rotorcraft regardless of weight',
         2: '''B : Gliders, Sailplanes, airships, baloons, parachutists/skydivers, hang-gliders, paragliders
         unmanned aerial vehicles'''}

        return {"Category":mapping[prediction]}

    except Exception as e:
        
        return {"Error during prediction": str(e), "Data": data}

@app.post("/query-data")
async def query_data(request:Request):
    
    try:
        data = await request.json()
        query = data.get("query")
        print(query)
        if not query:
            raise HTTPException(status_code=400, detail= "No query provided")
        
        data = query_database(query)

        return {"Data":data}
    

    except Exception as e:
        return {"Error": str(e)}