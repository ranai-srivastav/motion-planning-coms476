import dubins
import numpy
import matplotlib.pyplot as plt

qI = (1, 1, 0)
qG = (1, 2, 0)

p = dubins.shortest_path(qI, qG, 0.5)

marker_style = dict(linestyle=':', color='0.8', markersize=10,
                    markerfacecolor="tab:blue", markeredgecolor="tab:blue")

# plt.plot(qI[0], qI[1], marker = (3, 0, numpy.degrees(qI[2])))
# plt.plot(qG[0], qG[1], marker = (3, 0, numpy.degrees(qG[2])))
plt.plot(qG[0], qG[1], marker=MarkerStyle('$f$', 'left', 0), **marker_style)
# q, t = dubins.path_sample(qI, qG, 0.5, 0.01)
# x = [states[0] for states in q]
# y = [states[1] for states in q]

# plt.plot(x, y, 'b-')

# print("starting")
# for i in range(len(q)):
#     # plt.plot(q[i][0], q[i][1], marker = (3, 0, q[i][2]))

# plt.plot(x, y, '-b')

plt.show()
