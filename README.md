# Project idea 1

## Welcome to my data science project. I'm still exploring options for this repo, but I think that I'll be looking into the project described below.

### Tampa Area Flight Patterns

Using ADSB and potentially meteorological data, I want to investigate

- If there are is any predictability behind flight delays in the Tampa Bay area
- If it is possible to classify aircraft type/category based on flight patterns (speed, altitude ... etc.)
- Any emergency or alert indicators and the possibility of predicting them

# Project idea 2
- if there is any predictability behind which ships are at risk of Houthi attacks
- which ships are specifically NOT at risk of Houthi attacks
- patterns in attack frequency of Houthi attacks
    - Identify if changes in frequency or scale are related to other events (using GDELT)
    - Determine whether changes in frequency or scale are predictable
- Identify outside impacts (US or Saudi interventions in Yemen, Iraq, and Iran) on attack patterns of Houthi attacks
    - Methods, frequency, or scale
    - Investigate other outside impacts: e.g. Current Russian relationship with Iran, and it’s potential impacts on Russian shipping
- Data:
    - Use ACLED to search through the “notes” to identify Houthi attacks
        - Potential opportunity for feature engineering to better understand the methods used in attacks, their frequency, and the scale of the attacks
        - Identify the International Maritime Organization (IMO) ship identification number and use it to obtain ship information from the KPLER dataset
    - Use KPLER to identify cargo types, owner of the vessel, recent charters, recent ports visited, sanction risks, and other information that could be useful in predicting Houthi attacks
        - This is going to require some research to understand how these factors relate to the potential of a Houthi attack, and **if they’re worth including in the model**
        - MARINE TRAFFIC can also be used to supplement KPLER data and information
    - Potentially use GDELT to obtain more information about specific attacks, and the Houthi rational behind the attacks.
- Deliverables:
    - Streamlit app telling the “story” of a couple of attacks (showing hour by hour or day by day activity on a map for each attack)
    - Modeling results and predictability of Houthi attacks
- Limitations
    - ACLED data is only available for the past year, and I estimate that there are only ~ 412 different attacks to work with, which is a very small amount of data
    - No access to KPLER api yet, so can only look at attacks one by one
