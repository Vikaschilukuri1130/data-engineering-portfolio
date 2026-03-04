import pandas as pd

def transform_sales_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna(0)

    # Create calculated column
    if 'quantity' in df.columns and 'price' in df.columns:
        df['total_sales'] = df['quantity'] * df['price']

    print("Transformation completed")

    return df
