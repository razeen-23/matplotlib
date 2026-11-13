import matplotlib.pyplot as plt
months = ["jan","feb","mar","apr","jun"]
sales = [120,150,170,180,230]
plt.plot(months,sales)
plt.title("monthly sales")
plt.xlabel("month")
plt.ylabel("sales(units)")
plt.show()
