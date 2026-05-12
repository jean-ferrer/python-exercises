# 2026-05-12

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    n_of_orders = orders.value_counts('customer_number')

    result = {"customer_number": [n_of_orders.index[0]]}

    result = pd.DataFrame(result)

    return result