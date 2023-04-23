# How k-NN algorithm works

In human terms, the algorithm works as "You will become like the people you associate with". Simply said you have some dataset, each datapoint and the datapoint M you want to classify has an x and y value (in 2D space), then you calculate distances from datapoint M to other datapoints in dataset with euclidean distance, that is distance = √(x2 - x1)²+(y2 - y1)² where x2, y2 are position for dataset point and x1, y1 is for datapoint M. After that you find k smallest distances from these calculated distances then find most repeatable class and assign this class to datapoint M. That's the simple explanation.

## Program
Program starts by importing numpy for array, matplotlib for graphing dataset and math for sqrt() function
``` 
import numpy as np
import matplotlib.pyplot as plt
import math
```
Then we declare function for calculating distance, it takes 4 arguments x and y for unknown datapoint and x and y for known datapoint
```
def dis(x, y, X, Y):
    return math.sqrt((x - X) ** 2 + (y - Y) ** 2)

```

Dataset looks like this:
```
data = np.array([[110, 55, "auto", None], [113, 68, "auto", None], [119, 67, "auto", None], [119, 60, "auto", None], [139, 70, "auto", None], [130, 81, "auto", None], [146, 90, "bus", None], [152, 88, "bus", None], [162, 95, "bus", None], [144, 91, "bus", None], [158, 83, "bus", None], [167, 93, "bus", None], [175, 99, "track", None], [172, 95, "track", None], [180, 95, "track", None], [182, 97, "track", None], [170, 94, "track", None]])

x = np.array([data[0][0], data[1][0], data[2][0], data[3][0], data[4][0], data[5][0], data[6][0], data[7][0], data[8][0], data[9][0], data[10][0], data[11][0],data[12][0], data[13][0], data[14][0], data[15][0], data[16][0]])
y = np.array([data[0][1], data[1][1], data[2][1], data[3][1], data[4][1], data[5][1], data[6][1], data[7][1], data[8][1], data[9][1], data[10][1], data[11][1], data[12][1], data[13][1], data[14][1], data[15][1], data[16][1]])

objekt = np.array([160, 75, None])
k = 5
```
Data has x and y coordinates, class name and None is for calculated distance. x and y arrays are just for plotting coordinates. objekt is an object we want to classify.

```
distances = []
cls = []
for bod in data:
    bod[3] = dis(bod[0], bod[1], objekt[0], objekt[1]) if bod[3] == None else Exception
    distances.append(bod[3])

for i in range(k):
    min_dis = min(distances)
    index = distances.index(min_dis)
    cls.append(data[index])
    distances.pop(index)
    distances.insert(index, float("inf"))
```
In first for loop we calculate distances and store then in distances array. In second for loop we are looking for k smallest distances, then we store these objects in cls array.

```
classes = [i[2] for i in cls]

car, bus, track = 0, 0, 0
for i in classes:
    car += 1 if i == "auto" else 0
    bus += 1 if i == "bus" else 0
    track += 1 if i == "track" else 0

if car > max(bus, track):
    objekt[2] = "auto"

else:
    if bus > max(car, track):
        objekt[2] = "bus"

    else:
        objekt[2] = "track"

print(objekt)
```
Here firstly we are interested only in class ("auto", "bus", "track"), not hole objects, then in for loop for every class we increase respective variable by 1. Lastly we need to find out most numerous variable and assign class to our uknown object.

```
plt.scatter(np.sort(x), np.sort(y))

plt.show()
```
At the end of program we plot all coordinates with matplotlib.
