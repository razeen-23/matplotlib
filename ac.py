import matplotlib.pyplot as plt

products = ["laptop", "phone", "watch", "tablets"]
units_sold = [35,60,25,40]
plt.barh(products,units_sold, color="steelblue")
plt.title("products sold")
plt.xlabel("products")
plt.ylabel("units sold")
plt.show()