import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Step 1: Create Dataframes

# customers - Dataframe
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5], 
    'customer_name': ['Alice', 'Bob', 'Vishal', 'Ganesh', 'Waseef Ahmed'], 
    'country': ['USA', 'Europe', 'India', 'India', 'UAE']
})

print(customers)

# products - Dataframe
products = pd.DataFrame({
    'product_id': [1001, 1002, 1003, 1004, 1005], 
    'product_name': ['Tooth Paste', 'Laptop', 'Mouse', 'Knife', 'Towel'], 
    'category': ['Daily Usage', 'Electronics', 'Electronics', 'Kitchen Acessory', 'Clothes'], 
    'price': [40, 50000, 600, 250, 80]
})

print(products)

# orders - Dataframe
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105], 
    'customer_id': [5, 3, 4, 4, 1], 
    'product_id': [1004, 1001, 1002, 1003, 1001], 
    'quantity': [3, 2, 1, 1, 3], 
    'order_date': [datetime.now() - timedelta(i*10) for i in range(5)]
})

print(orders)

# Step 2: Transformations and Joins
orders['total_amount'] = orders['quantity'] * orders['product_id'].map(products.set_index('product_id')['price'])

# Join orders with customers to get customers details for each order
orders_with_customers = pd.merge(orders, customers, on='customer_id', how='left')

print(orders_with_customers)