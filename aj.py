import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales.csv")
plt.plot(df["month"], df["revenue"], marker="o")
plt.title("Revenue by Month")
plt.xlabel("month")
plt.ylabel("revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()