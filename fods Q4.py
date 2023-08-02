import numpy as np


sales_data = np.array([10000, 15000, 12000, 18000])


total_sales_year = np.sum(sales_data)

percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print(f"Total sales for the year: {total_sales_year}")
print(f"Percentage increase in sales from the first quarter to the fourth quarter: {percentage_increase:.2f}%")
