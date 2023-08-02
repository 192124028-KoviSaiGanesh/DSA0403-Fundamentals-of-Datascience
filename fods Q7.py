import pandas as pd


data = {
    'customer_id': [1, 2 ,3,1],
    'order_date': ['2023-08-01', '2023-08-01', '2023-08-02','2023-08-02'],
    'product_name': ['Product A', 'Product B', 'Product C','Product B'],
    'order_quantity': [2, 3, 1,3]
}

order_data = pd.DataFrame(data)
print(order_data)


total_orders_by_customer = order_data.groupby('customer_id').size()
print("Total orders by each customer:")
print(total_orders_by_customer)


av=order_data.groupby(by='product_name')
average=av['order_quantity'].mean()
print(average)

earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("Earliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
