import matplotlib.pyplot as plt

channels = ["Website", "Instagram", "Referral", "Walk-in"]
leads = [40, 30, 20, 10]
plt.pie(leads, labels=channels, autopct="%1.1f%%", startangle=90)
plt.title("Lead Sources")
plt.show()