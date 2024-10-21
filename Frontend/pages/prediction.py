import streamlit as st
import pandas as pd
import requests

if st.sidebar.button("Reset Page"):
    st.markdown(
        """
        <script>
        document.documentElement.scrollTop = 0;
        </script>
        """,
        unsafe_allow_html=True,
    )

LAT = 27.9506
LONG = -82.4572

emergency = st.selectbox("Emergency Status:", ["No Emergency", 
                                               "General Emergency",
                                               "Lifegaurd/Medical",
                                               "Minimum Fuel",
                                               "No Comms",
                                               "Unlawful Interference"])
em_map = {"No Emergency":0, 
        "General Emergency":1,
        "Lifegaurd/Medical": 2,
        "Minimum Fuel": 3,
        "No Comms": 4,
        "Unlawful Interference": 5}

gs = st.slider("Ground Speed (knots):", 0.0, 1000.0, 350.0)

nac_p = st.slider("Navigation Accuracy Category (Position):", 0.0, 10.0, 5.0)

aircraft_type = st.text_input("Aircraft Type (e.g., A320, B737, etc.):", value=90)

#90% of the dataset has alert == 3, and until I figure out what alerts mean,
#default value is going to be 3
alert = 3

baro_rate = st.slider("Barometric Rate (feet/min):", -6000.0, 6000.0, 0.0)

alt_baro = st.slider("Barometric Altitude (feet):", 0.0, 45000.0, 10000.0)

track = st.slider("Track (degrees):", 0.0, 360.0, 150.0)

alt_geom = st.slider("Geometric Altitude (feet):", 0.0, 45000.0, 10000.0)

geom_rate = st.slider("Geometric Rate (feet/min):", -6000.0, 6000.0, 0.0)

nav_altitude_mcp = st.slider("MCP/FCU Selected Altitude (feet):", 0.0, 45000.0, 10000.0)

nac_v = st.slider("Navigation Accuracy Category (Velocity):", 0.0, 10.0, 5.0)

flight = st.text_input("Flight Number (Optional):", value="1234")
if flight == "":
    flight = 1234
hex_code = st.text_input("Hex Code (Optional):", value="1234")
if hex_code == "":
    hex_code = 1234

user_input_features = {
    "lon": LONG,
    "emergency": em_map[emergency],
    "flight": int(flight),
    "nac_p": nac_p,
    "gs": gs,
    "t": aircraft_type,
    "alert": alert, #defalt value of 3
    "baro_rate": baro_rate,
    "alt_baro": alt_baro,
    "track": track,
    "hex": int(hex_code),
    "alt_geom": alt_geom,
    "lat": LAT,
    "geom_rate": geom_rate,
    "nav_altitude_mcp": nav_altitude_mcp,
    "nac_v": nac_v,
}

if st.button("Predict"):
    st.write("Predicting now!")

    response = requests.post(
        "http://fastapi_route:5001/predict-data",
        json = user_input_features,
        timeout=10
    )
    if response.status_code == 200:

        result = response.json()
        st.write(result)

    else:
        st.error(f"Failed to get prediction: {response.status_code}")
        st.write(f"Error details: {response.text}")       