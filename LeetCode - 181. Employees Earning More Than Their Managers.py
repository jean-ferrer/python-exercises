# 2026-05-06

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    employee = employee[employee['salary'] > employee['managerId'].map(employee.set_index('id')['salary'])]
    employee = employee['name'].to_frame('Employee')
    
    return employee