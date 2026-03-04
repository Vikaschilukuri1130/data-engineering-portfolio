import pandas as pd
import sqlite3

def load_data(df):

    try:
        print("Loading data into database...")

        conn = sqlite3.connect("sales_database.db")

        df.to_sql("sales_data", conn, if_exists="replace", index=False)

        conn.close()

        print("Data loaded successfully")

    except Exception as e:
        print("Error loading data:", e)
