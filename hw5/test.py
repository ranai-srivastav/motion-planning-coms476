import dubins
import numpy
import matplotlib.pyplot as plt
from matplotlib.markers import *
from edge import DubinsEdge

qI = (1, 1, 0)
qG = (1, 2, numpy.pi/6)

p = dubins.shortest_path(qI, qG, 0.5)

plt.plot(qI[0], qI[1], marker = (3, 0, numpy.degrees(qI[2])))
plt.plot(qG[0], qG[1], marker = (3, 0, numpy.degrees(qG[2])))

q, t = dubins.path_sample(qI, qG, 0.5, 0.1)
for i in range(len(q)):
    print(f"{q[i]}   {t[i]}")

# x = [states[0] for states in q]
# y = [states[1] for states in q]
# plt.plot(x, y, 'b-')

# print(p.path_length())

# edge = DubinsEdge(qI, qG, 0.5, 0.1)
# print(edge.get_discretized_state(20))

# print(type(edge.split(2)))
# q, t = edge.split(2).sample_many(0.1)
# x = [states[0] for states in q]
# y = [states[1] for states in q]
# plt.plot(x, y, 'r-')
# print(edge.split(2))

plt.show()
