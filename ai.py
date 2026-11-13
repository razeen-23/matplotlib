import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 130, 125, 160]
plt.plot (months, sales, marker="o")
plt.title("monthly sales")
plt.savefig("monthly_sales.png", dpi=300, bbox_inches="tight")
plt.show()

