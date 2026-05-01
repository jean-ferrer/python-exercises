# 2026-04-21

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    
    ids = person["email"]
    duplicates = person[ids.isin(ids[ids.duplicated()])].sort_values("email")
    duplicates = duplicates.drop_duplicates(subset="email")
    return duplicates[["email"]]