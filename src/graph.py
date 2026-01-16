import matplotlib.pyplot as plt
import numpy as np

from data import DataHandling

data = DataHandling()

x_list = data.get_data_of_how_many_students_in_class()
y_list = data.get_count_of_each_hour_of_math()

x = np.array(x_list)
y = np.array(y_list)

plt.scatter(x, y)

m, b = np.polyfit(x, y, 1)

data.add_linear_equation(m, b)

plt.plot(x, m*x + b, color='red')

r = np.corrcoef(x, y)[0, 1]
data.add_r_value(r)

plt.xlabel("Students Per Class")
plt.ylabel("Number of students who like math")
plt.title("Number of students who like math vs Students Per Class")
plt.show()