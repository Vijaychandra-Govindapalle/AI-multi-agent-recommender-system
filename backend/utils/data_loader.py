import pandas as pd
import ast

def load_customers(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df['Browsing_History'] = df['Browsing_History'].apply(ast.literal_eval)
    df['Purchase_History'] = df['Purchase_History'].apply(ast.literal_eval)
    return df

def load_products(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df['Similar_Product_List'] = df['Similar_Product_List'].apply(ast.literal_eval)
    return df
