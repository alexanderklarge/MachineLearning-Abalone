import pandas as pd

def snake_case(df):
    """Enforce snake_case formatting on all dataframe column names"""
    snake_case_column_names = []

    for col in df.columns:
        col = col.lower()
        col = col.replace(" ", "_")
        snake_case_column_names.append(col)

    df.columns = snake_case_column_names
    return df