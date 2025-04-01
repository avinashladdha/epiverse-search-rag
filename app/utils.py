import pandas as pd

def get_value(df: pd.DataFrame, column: str, condition: pd.Series):
    try:
        return df.loc[condition, column].iloc[0]
    except IndexError:
        return None