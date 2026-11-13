import matplotlib.pyplot as plt

products = ["laptop", "phone", "watch", "tablets"]
units_sold = [35,60,25,40]
plt.bar(products,units_sold, color="steelblue")
plt.title("products sold")
plt.xlabel("products")
plt.ylabel("units sold")
plt.show()

# import matplotlib.pyplot as plt

# products = ["Laptop", "Phone", "Tablet", "Watch"]
# units_sold = [35, 60, 25, 40]
# plt.bar(products, units_sold, color="steelblue")
# plt.title("Units Sold by Product")
# plt.xlabel("Product")
# plt.ylabel("Units Sold")
# plt.show()