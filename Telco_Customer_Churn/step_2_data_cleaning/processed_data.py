# Import Packages
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def processed_data():
    # Read dataset
    df = pd.read_csv("telco-cust-churn-dataset-for-cleaning.csv")

    # Empty dummy columns list
    col_list = list(df.columns)
    encode_list = []

    # Fill the dummy list with categorical variables 
    # Assumption if there are no more than 3 unique categories in the column
    for col in col_list:
        if df[col].nunique() <= 3:
            encode_list.append(col)

    ## Encoder
    label_encoder = LabelEncoder()

    # Create a DataFrame with the encoded columns
    df_proc = df.copy()
    for col in encode_list:
        df_proc[col] = label_encoder.fit_transform(df[col])

    df_proc = df_proc.drop('Unnamed: 21', axis=1)

    return df_proc


