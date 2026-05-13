# 2026-05-13

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    
    employee = employee.drop(columns=['supervisor', 'salary'])

    merge = pd.merge(employee, bonus, how='left')
    merge = merge.drop(columns=['empId'])
    
    merge = merge[(merge['bonus'].isnull()) | (merge['bonus'] < 1000)]

    return merge