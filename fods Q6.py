import numpy as np


item_prices = np.array([2.50, 3.75, 1.99, 4.25])
item_quantities = np.array([3, 2, 5, 1])
discount_rate = 10  
tax_rate = 7.5      


subtotal = np.dot(item_prices, item_quantities)


discount_amount = subtotal * (discount_rate / 100)


total_before_tax = subtotal - discount_amount


tax_amount = total_before_tax * (tax_rate / 100)


final_total_cost = total_before_tax + tax_amount


print("Subtotal: ${:.2f}".format(subtotal))
print("Discount amount: ${:.2f}".format(discount_amount))
print("Total amount before tax: ${:.2f}".format(total_before_tax))
print("Tax amount: ${:.2f}".format(tax_amount))
print("Final total cost: ${:.2f}".format(final_total_cost))
