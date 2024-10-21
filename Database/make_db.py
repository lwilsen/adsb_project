"""Convert the data into a sqlite database here"""

import sqlite3
import pandas as pd

combined_df = pd.read_csv("adsb_data/combined_df.csv")
cleaned_df = pd.read_csv("./adsb_data/preprocessed_ads_b_data.csv")

'''Data Processing'''

cleaned_df['category'] = cleaned_df[cleaned_df.columns[28-12:28]].idxmax(axis=1).astype('float64')

num_to_num = {
    0: 0,
    1: 1,
    2: 3,
    3: 14,
    4: 15,
    5: 20,
    6: 16,
    7: 10,
    8: 2,
    9: 2,
    11: 2,
    10: 2
}

cleaned_df['category'] = cleaned_df.category.map(num_to_num).astype('float64')
cleaned_df.drop(cleaned_df.columns[28-12:28], axis=1, inplace=True)


conn = sqlite3.connect("adsb_data.db")

combined_df.to_sql("combined_data", conn, if_exists="replace", index=False)
cleaned_df.to_sql("cleaned_data", conn, if_exists="replace", index=False)

conn.commit()
conn.close()