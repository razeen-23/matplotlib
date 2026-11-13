import matplotlib.pyplot as plt

marks = [45,49,56,67,69,74,77,87,86,88,92,96]
plt.hist(marks, bins=5, edgecolor="black")
plt.title("distrubtion in student marks")
plt.xlabel("marks")
plt.ylabel("number of students")
plt.show()