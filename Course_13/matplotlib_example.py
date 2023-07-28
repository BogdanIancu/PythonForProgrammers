import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
sales_product_a = [100, 120, 150, 180, 200, 210, 230]
sales_product_b = [80, 90, 110, 130, 150, 170, 190]

plt.plot(years, sales_product_a, label='Product A')
plt.plot(years, sales_product_b, label='Product B')

plt.xlabel('Years')
plt.ylabel('Sales')
plt.title('Product Sales Over the Years')
plt.legend()
plt.show()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
product_a_sales = [200, 300, 400, 350, 250]
product_b_sales = [150, 250, 350, 300, 200]

plt.bar(months, product_a_sales, label='Product A')
plt.bar(months, product_b_sales, bottom=product_a_sales, label='Product B')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Comparison')
plt.legend()
plt.show()

