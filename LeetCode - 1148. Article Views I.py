# 2024-12-24

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    self_views = views[views['author_id'] == views['viewer_id']]
    
    result = self_views['author_id'].drop_duplicates().sort_values().reset_index(drop=True)
    
    return pd.DataFrame({'id': result})