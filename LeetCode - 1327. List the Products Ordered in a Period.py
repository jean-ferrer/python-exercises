# 2026-04-28

import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    orders_feb = orders.query("order_date >= '2020-02-01' and order_date <= '2020-02-29'")

    orders_feb = orders_feb.drop(columns=['order_date'])
    products = products.drop(columns=['product_category'])

    orders_products = pd.merge(orders_feb, products)
    orders_products = orders_products.groupby('product_name')
    orders_products = orders_products[['unit']].sum().reset_index()
    orders_products_filtered = orders_products[orders_products['unit'] >= 100]

    return orders_products_filtered