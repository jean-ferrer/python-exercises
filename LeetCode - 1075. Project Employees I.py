# 2026-05-01

import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    
    employee = employee.drop(columns=["name"])
    
    work = pd.merge(project, employee)
    work = work.drop(columns=["employee_id"])
    
    work_xp = work.groupby(["project_id"]).mean().reset_index()
    work_xp = work_xp.rename(columns={"experience_years": "average_years"})
    work_xp = work_xp.round(2)
    
    return work_xp