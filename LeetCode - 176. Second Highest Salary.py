# 2026-04-23

import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    count = employee.count()
    if count.id <= 1:
        data = {"SecondHighestSalary": [None]}
        secHighestSalary = pd.DataFrame(data)

        return secHighestSalary

    def is_unique(df):
        a = df.to_numpy()
        return (a[0] == a).all()

    is_unique = is_unique(employee['salary'])

    if is_unique:
        data = {"SecondHighestSalary": [None]}
        secHighestSalary = pd.DataFrame(data)

        return secHighestSalary

    else:
        data = {"SecondHighestSalary": [0]}
        secHighestSalary = pd.DataFrame(data)

        employee = employee.drop_duplicates(subset=["salary"])

        employee = employee.sort_values(by=["salary"], ascending=False)
        row = employee.iloc[min(len(employee), 2)-1]

        secHighestSalary = secHighestSalary.replace(0, row.salary)

        return secHighestSalary