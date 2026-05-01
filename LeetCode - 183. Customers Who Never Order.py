# 2026-04-26

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(customers, orders, how='left',left_on='id', right_on='customerId')

    df = df.drop(columns=['id_x', 'id_y'])

    df = df[df['customerId'].isnull()]

    df = df.drop(columns=['customerId'])

    df = df.rename(columns={'name': 'Customers'})

    return df