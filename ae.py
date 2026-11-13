import matplotlib.pyplot as plt

study_hours = [1, 2, 2, 3, 4, 5, 6, 7]
marks = [42, 48, 55, 58, 66, 73, 81, 90]
plt.scatter(study_hours,marks, color="darkorange")
plt.title("study hours vs marks")
plt.xlabel("study hours")
plt.ylabel("marks")
plt.show()