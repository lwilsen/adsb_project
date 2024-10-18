"""Convert the data into a sqlite database here"""

import sqlite3
import pandas as pd

combined_df = pd.read_csv("adsb_data/combined_df.csv")
cleaned_df = pd.read_csv("adsb_data/processed_df.csv")

conn = sqlite3.connect("adsb_data.db")

combined_df.to_sql("combined_data", conn, if_exists="replace", index=False)
cleaned_df.to_sql("cleaned_data", conn, if_exists="replace", index=False)

conn.commit()
conn.close()