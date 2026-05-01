# 2026-04-27

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    sales_person = sales_person.drop(columns=['commission_rate', 'hire_date'])
    company = company.drop(columns=['city'])
    orders = orders.drop(columns=['order_date', 'amount'])

    company_and_orders = pd.merge(company, orders)

    company_red = company_and_orders[company_and_orders['name'] == 'RED']
    company_red = company_red.drop(columns=['name', 'com_id', 'order_id'])

    sales_person = pd.merge(sales_person, company_red, how='left', indicator=True)
    sales_person = sales_person[sales_person['_merge'] == 'left_only'].drop(columns=['sales_id', 'salary', '_merge'])
    
    return sales_person