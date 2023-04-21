import dubins
import numpy
import matplotlib.pyplot as plt
from matplotlib.markers import *
from edge import DubinsEdge

qI = (1, 1, 0)
qG = (2, 2, 0)

p = dubins.shortest_path(qI, qG, 0.5)

fig, ax = plt.subplots(1)

ax.plot(qI[0], qI[1], marker = (3, 0, numpy.degrees(qI[2])))
ax.plot(qG[0], qG[1], marker = (3, 0, numpy.degrees(qG[2])))

# q, t = dubins.path_sample(qI, qG, 0.5, 0.1)
q, t = p.sample_many(0.1)
# for i in range(len(q)):
#     print(f"{q[i]}   {t[i]}")

q.append(qG)
# t.append(p.path_length())

print(p.path_length())
print(len(t))
print(t)

x = [states[0] for states in q]
y = [states[1] for states in q]
ax.plot(x + [qG[0]], y + [qG[1]], 'b-')
# ax.plot(x, y, 'b-')

# edge = DubinsEdge(qI, qG, p.path_length(), q, t, 0.1, 0.1)
# point = edge.get_nearest_point((3, 1.5, 0), ax)

# plt.plot(point[0][0], point[0][1], 'ko' )


# print(p.path_length())

# print(edge.get_discretized_state(20))

# print(type(edge.split(2)))
# q, t = edge.split(2).sample_many(0.1)
# x = [states[0] for states in q]
# y = [states[1] for states in q]
# plt.plot(x, y, 'r-')
# print(edge.split(2))

plt.show()
