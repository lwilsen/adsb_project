import streamlit as st

st.title("ADS-B Data Science Project")
st.write("Luke Wilsen")
st.divider()

st.header('''**Project Goal**''')
st.write('''- Explore patterns and predictability of ADS-B data, sourced from their online API''')

st.subheader("About the Data")
st.write('''
- This data contains information about aircraft and was obtained from an online API of ADSB data, courtesy of Brett Waugh. (Thanks Brett!)

### What is ADS-B Data?

ADS-B (Automatic Dependent Surveillance–Broadcast) is a surveillance technology used in aviation for tracking aircraft. It provides precise location and status information through messages transmitted by aircraft and picked up by ground stations or satellites.

Below is a detailed explanation of the different fields available in the data.

---

## Basic Aircraft Information

- **`hex`**: A unique hexadecimal identifier assigned to each aircraft, acting as a digital fingerprint.  
- **`type`**: The type of ADS-B message (e.g., `adsb_icao` for standard ICAO-formatted messages).  
- **`flight`**: The flight number assigned to the aircraft.  
- **`r`**: The aircraft's registration number (combination of letters and numbers).  
- **`t`**: The aircraft type or model designation (e.g., Boeing 737).  
- **`alt_baro`**: Barometric altitude in feet.  
- **`alt_geom`**: Geometric altitude in feet, calculated from GPS data for higher accuracy.  
- **`gs`**: Ground speed of the aircraft in knots.  
- **`track`**: Heading of the aircraft in degrees, measured clockwise from north.  
- **`baro_rate`**: Rate of climb or descent in feet per minute.  
- **`squawk`**: Four-digit code for aircraft identification and coordination, used for emergencies or special conditions.  
- **`emergency`**: Indicates whether the aircraft has declared an emergency.  
- **`category`**: Classification of the aircraft based on size and type.  

---

## Position and Navigation Data

- **`lat`**: Latitude in degrees.  
- **`lon`**: Longitude in degrees.  
- **`nic`**: Number of independent components used for position determination (accuracy indicator).  
- **`rc`**: Receiver capability of the aircraft’s ADS-B equipment.  
- **`seen_pos`**: Time (in seconds) since the last position report.  
- **`version`**: Version of the ADS-B message format.

---

## Additional Navigation and Status Information

- **`nic_baro`**: NIC value used for barometric altitude determination.  
- **`nac_p`**: Navigation accuracy class for position (expected accuracy of position data).  
- **`nac_v`**: Navigation accuracy class for velocity (expected accuracy of velocity data).  
- **`sil`**: Surveillance information link capability of the aircraft.  
- **`sil_type`**: Type of SIL in use.  
- **`gva`**: Global vertical accuracy of the position data.  
- **`sda`**: Surveillance data availability, indicating transmission frequency and reliability.  
- **`alert`**: Indicates whether an alert has been issued for the aircraft.  
- **`spi`**: System performance indicator showing the health of the ADS-B system.  
- **`mlat`**: Multi-lateration data based on signals from multiple ground stations.  
- **`tisb`**: Terrestrial internet-based surveillance data.  

---

## Signal and Message Information

- **`messages`**: Total number of messages received from the aircraft.  
- **`seen`**: Time (in seconds) since the last message was received.  
- **`rssi`**: Received signal strength indicator (signal strength from the aircraft).  
- **`dbFlags`**: Data block flags, indicating the presence of specific data elements.  

---

## Calculated Metrics and Navigation Settings

- **`geom_rate`**: Geometric rate of climb or descent in feet per minute.  
- **`nav_qnh`**: QNH barometric pressure at the airport.  
- **`nav_altitude_mcp`**: Navigation altitude set on the aircraft's flight management computer (FMC).  
- **`nav_heading`**: Navigation heading in degrees.  
- **`nav_modes`**: Active navigation modes on the aircraft.  
- **`true_heading`**: True heading, accounting for wind direction and speed.  
- **`calc_track`**: Calculated track based on position and velocity.

---

This data can be used to 
- monitor aircraft movements, 
- analyze trends in flight patterns, 
- assist in research related to air travel. 
         
Enjoy exploring the data!''')
