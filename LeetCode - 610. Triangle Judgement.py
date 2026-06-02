# 2026-06-02

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    
    triangle['triangle'] = pd.Series(dtype='string')
    counter = 0

    for i in triangle.itertuples(index=False):
        if (i[0] >= i[1]+i[2]) or (i[1] >= i[0]+i[2]) or (i[2] >= i[0]+i[1]):
            triangle.at[counter, 'triangle'] = 'No'
            counter += 1
        else:
            triangle.at[counter, 'triangle'] = 'Yes'
            counter += 1

    return triangle