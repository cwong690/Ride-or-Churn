import numpy as np
import pandas as pd

def set_ohe(df:pd.DataFrame, col_name:str):
    for val in df[col_name].value_counts().index:
        df[f"{col_name}: {val}"] = df[col_name].map(lambda x: 1.0 if x==val else 0.0 )
    df.drop(df.columns[-1], axis=1, inplace=True)
    df.drop(columns=col_name, inplace=True)
    return df