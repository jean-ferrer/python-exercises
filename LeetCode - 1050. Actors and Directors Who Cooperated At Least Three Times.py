# 2024-12-19

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    coop = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')

    return coop[coop['count'] >= 3][['actor_id', 'director_id']]