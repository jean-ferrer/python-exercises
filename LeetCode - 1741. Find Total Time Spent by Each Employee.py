# 2024-12-17

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    
    total_time = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()
    
    total_time = total_time.rename(columns={'event_day': 'day', 'time_spent': 'total_time'})
    
    return total_time