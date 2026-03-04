import pandas as pd
import os

# Path to raw data
DATA_PATH = "sales-etl-pipeline/data/sales_data.csv"

def extract_sales_data():
    """
    Extract sales data from CSV file
    """
    try:
        print("Reading sales data...")

        df = pd.read_csv(DATA_PATH)

        print("Data extracted successfully")
        print(df.head())

        return df

    except Exception as e:
        print("Error extracting data:", e)
        return None


if __name__ == "__main__":
    data = extract_sales_data()

    if data is not None:
        print("Extraction complete")
