import csv
import matplotlib.pyplot as plt
import numpy as np


video_game_hours = []
sleep = []

with open("gaming_hours_vs_performance.csv", "r") as f:
    file = csv.reader(f)
    header = next(file)
    data = [row for row in file]
        
    for i in range(len(data)):
        try:
            if data[i][6] not in video_game_hours:
                video_game_hours.append(data[i][6])
                sleep.append(data[i][8])
        except IndexError:
            continue

video_game_hours = [float(i) for i in video_game_hours]
sleep = [float(i) for i in sleep]

x = np.array(video_game_hours)
y = np.array(sleep)

plt.scatter(x, y)

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red')


plt.xlabel("Video Game Hours")
plt.ylabel("Sleep")
plt.title("Video Game Hours vs Sleep")
plt.show()