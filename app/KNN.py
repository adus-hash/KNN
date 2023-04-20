import numpy as np
import matplotlib.pyplot as plt
import math

        # (x a y je preklasifikovany bod)
def dis(x, y, X, Y):
    dis = math.sqrt((x - X) ** 2 + (y - Y) ** 2)

    return dis


                    #auta                                                                                                       # busy                                                                                                     #track
data = np.array([[110, 55, "auto", None], [113, 68, "auto", None], [119, 67, "auto", None], [119, 60, "auto", None], [139, 70, "auto", None], [130, 81, "auto", None], [146, 90, "bus", None], [152, 88, "bus", None], [162, 95, "bus", None], [144, 91, "bus", None], [158, 83, "bus", None], [167, 93, "bus", None], [175, 99, "track", None], [172, 95, "track", None], [180, 95, "track", None], [182, 97, "track", None], [170, 94, "track", None]])


x = np.array([data[0][0], data[1][0], data[2][0], data[3][0], data[4][0], data[5][0], data[6][0], data[7][0], data[8][0], data[9][0], data[10][0], data[11][0],data[12][0], data[13][0], data[14][0], data[15][0], data[16][0]])
y = np.array([data[0][1], data[1][1], data[2][1], data[3][1], data[4][1], data[5][1], data[6][1], data[7][1], data[8][1], data[9][1], data[10][1], data[11][1], data[12][1], data[13][1], data[14][1], data[15][1], data[16][1]])


objekt = np.array([160, 75, None])  #137 je auto, 138 je uz bus
k = 5

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



plt.scatter(np.sort(x), np.sort(y))

plt.show()
