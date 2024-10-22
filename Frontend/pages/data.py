import requests

import streamlit as st
import pandas as pd

st.title("Data")

table_option = st.radio("Select Data",
                        ("Raw", "Cleaned"),
                        key = "table_option")

INPUT_QUERY = ""

if table_option == "Raw":
    INPUT_QUERY = "SELECT * FROM combined_data LIMIT 10;"
else:
    INPUT_QUERY = "SELECT * FROM cleaned_data LIMIT 10;"

query = st.text_area(label="Input SQL here", value=INPUT_QUERY)

if st.button("Submit"):
    response = requests.post("http://fastapi_route:5001/query-data",
                                 json={"query":query}, timeout=10)
    if response.status_code == 200:
        try:
            result = response.json()
            data_dict = result.get("Data", {})
            columns = data_dict.get("Columns", [])
            data = data_dict.get("Data",[])

            if data and columns:
                df = pd.DataFrame(data=data, columns=columns)
                st.table(df)

        except requests.exceptions.JSONDecodeError:
            st.error("Error: The response is not in JSON format.")
            st.write("Response content:", response.text)


         
    
