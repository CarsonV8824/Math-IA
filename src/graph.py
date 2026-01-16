import csv
import matplotlib.pyplot as plt
import numpy as np

from data import DataHandling

data = DataHandling()

actual_data = data.get_data_by_math()



x = np.array([1,2,3])
y = np.array([-1,2,5])

plt.scatter(x, y)

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red')


plt.xlabel("Hour of class")
plt.ylabel("Sleep")
plt.title("Video Game Hours vs Sleep")
plt.show()