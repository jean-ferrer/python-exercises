# 2026-04-22

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    merge = pd.merge(person, address, on="personId", how="left")
    merge = merge.drop(labels=["personId", "addressId"], axis=1)

    return merge