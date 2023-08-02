import pandas as pd

# Sample data creation and loading (Replace this with your actual data loading step)
data = {
    'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product D'],
    'Quantity': [10, 15, 5, 8, 12, 20],
    'Date': ['2023-07-01', '2023-07-02', '2023-07-10', '2023-07-15', '2023-07-18', '2023-07-25']
}
sales_data = pd.DataFrame(data)

# Convert 'Date' column to datetime type
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Assuming today is August 2nd, 2023 and we want to analyze data for July 2023
current_date = pd.to_datetime('2023-08-02')

# Step 1: Filter data for the past month
past_month_data = sales_data[sales_data['Date'] >= current_date - pd.DateOffset(months=1)]

# Step 2: Group by 'Product' and sum 'Quantity'
product_sales = past_month_data.groupby('Product')['Quantity'].sum()

# Step 3: Sort products by total sales in descending order
top_5_products = product_sales.sort_values(ascending=False).head(5)

# Step 4: Display the top 5 products
print(top_5_products)
