import dubins
import numpy
import matplotlib.pyplot as plt
import random
from matplotlib.markers import *
from edge import DubinsEdge
from planning import DubinsEdgeCreator, DubinsDistanceComputator, stopping_configuration, ObstacleCollisionChecker
from graph import Tree
from obstacle import CircularObstacle
from draw_cspace import draw

qI = (-2, -0.5, 0)
qG = (2, -0.5, numpy.pi/2)
cspace = [(-3, 3), (-1, 1), (0, 2 * numpy.pi)]

list_of_points = \
            [
                [0.47018908,0.13233473,3.22148458],
                [1.87448827, 0.65099382, 2.31553196],
                [-1.28233491,  0.39840305,  2.8991513 ],
                [-1.7788868  ,-0.75160197,  5.30505463],
                [-2.92640689  ,0.72050493,  4.89921565],
                [-0.84814077, -0.2798563 ,  5.97388333],
                [-2.38293913, -0.94468893,  2.27267896],
                [-2.51619095, -0.81709146,  3.67249977],
                [-0.23176883, -0.94214081,  2.08501694],
                [-0.80774876, -0.3973958 ,  3.6173273 ],
                [0.28339864, 0.38829715 ,5.02384514],
                [ 2.54089493, -0.28423372,  2.19268261],
                [-0.66115372,  0.65683175,  5.1975254 ],
                [0.57525481, 0.87885312 ,1.20305807],
                [0.36859249, 0.59488329 ,2.73317702],
                [-0.31432487, -0.87139662,  0.87495558],
                [-0.22249576, -0.26156689,  3.52697805],
                [-1.31906585,  0.9381694 ,  0.54791334],
                [ 2.26024148, -0.97744914,  5.39570318],
                [0.87125132, 0.30631521 ,3.08322018],
                [-1.16630348, -0.26133009,  1.28486029],
                [-2.01194668, -0.24108816,  3.24769273],
                [0.41621843, 0.14500646 ,0.6075948 ],
                [-1.3501653,  -0.07404314,  1.3689335 ],
                [ 1.72256718, -0.62309758,  5.70417834],
                [ 0.84236501, -0.86843723,  3.59803924],
                [ 1.26180524, -0.57984315,  6.15715166],
                [ 2.76689412, -0.51431703,  5.82909527],
                qG,
                [-0.71947277, -0.76755832,  0.48912488],
                [ 0.86053256, -0.72219635,  0.34013911],
                [ 0.66511354, -0.2463904 ,  1.25257621],
                [-0.88287542,  0.08511088,  0.8242704 ],
                [-0.23039907, -0.65681921,  2.88402112],
                [ 1.98336499, -0.81787966,  2.58756304],
                [ 1.48125607, -0.10241091,  0.65370959],
                [1.01353674, 0.54743035 ,5.41359478],
                [-0.23576786,  0.91817888,  0.51830996],
                [-0.54678867, -0.28724936,  2.69171444],
                [ 1.78346297, -0.8384926 ,  0.78384094],
                [1.9240697,  0.67874508 ,4.4058966 ],
                [0.6439905,  0.98197989 ,4.67304174],
                [ 0.64993846, -0.29855123,  5.33067864],
                [ 0.24135599, -0.72033196,  1.06339191],
                [-0.08562195,  0.06790851,  4.22830163],
                [1.95618606, 0.01822925 ,2.98513348],
                [ 1.71416659, -0.2519369,   0.4646798 ],
                [-1.58170068, -0.92937456,  5.48755225],
                [ 2.5737982 , -0.45047543,  2.7694674 ],
                [-0.69748905, -0.37086829,  2.84512097],
                [-2.29454838,  0.77887494,  5.74743171],
                [-2.49598608,  0.66298738,  3.40573503],
                [-2.79236832,  0.71628988,  1.07352067],
                [1.60177771, 0.28465791 ,1.10001896],
                [ 0.90761765, -0.65435827,  1.92185284],
                [-2.58937477, -0.44717497,  2.25581947],
                [-1.61199714,  0.15248131,  1.36124835],
                [-1.8701531,  -0.44162231,  3.50478631],
                [ 1.20530976, -0.41853874,  3.02655924],
                [0.29502962, 0.80652081 ,4.55953172],
                [ 2.65542939, -0.96242705,  1.29815107],
                [-0.40194554, -0.14430867,  4.34248745],
                [-2.36850432, -0.16769629,  5.19424082],
                [0.45122347, 0.61238138 ,6.15651042],
                [-0.43043881, -0.57546238,  0.88152415],
                [-2.14808068, -0.24074963,  2.28768406],
                [ 2.07084754, -0.18110355,  1.5725693 ],
                [-0.72949626,  0.31819678,  4.38184168],
                [-2.20910568, -0.34205823,  1.79972913],
                [ 1.51284266, -0.50343879,  4.82849057],
                [-1.5110237,   0.93454518,  3.77449791],
                [ 1.92521978, -0.84333283,  3.74044559],
                [-0.82521283, -0.27766214,  0.38633755],
                [ 1.24358465, -0.06968637,  3.59629355],
                [ 1.72159385, -0.14035756,  5.75960038],
                [-1.92909007, -0.99356019,  1.55247178],
                [-1.22830329, -0.07740594,  2.27546519],
                [-0.16096421,  0.35494182,  2.57379274],
                [-0.75346969, -0.32949904,  3.21768418],
                [2.63638663, 0.84938968 ,5.00175324],
                [-2.92224375, -0.69327167,  4.86670893],
                [-2.98768865, -0.27923197,  5.69142609],
                [-0.24231153, -0.43221163,  0.60720776],
                [ 1.88601619, -0.33904753,  5.8960288 ],
                [0.73770813 ,0.60316617 ,2.7756055 ],
                [-0.83860533,  0.39249052,  5.39498745],
                [2.31347473 ,0.30879421, 1.0097488 ],
                [-2.96758936, -0.63318415,  0.82860129]
            ]    
    
def construct_circular_obstacles(dt):
    r = 1 - dt  # the radius of the circle
    c = [(0, -1), (0, 1)]  # the center of each circle
    t = [(0, numpy.pi), (-numpy.pi, 0)]  # range of theta of each circle
    obstacles = []
    for i in range(len(c)):
        obstacles.append(CircularObstacle(c[i], r, t[i]))
    return obstacles
    
list_of_constructed_obstacles = construct_circular_obstacles(0.2)
edge_creator = DubinsEdgeCreator(None, 0.1, 0.5)
distance_computator = DubinsDistanceComputator(0.5)
collision_checker = ObstacleCollisionChecker(list_of_constructed_obstacles)
boundaries = [obstacle.get_boundaries() for obstacle in list_of_constructed_obstacles]
tol = 1e-3
pG = 0.1

fig, ax = plt.subplots(1)

# plt.plot([x for x, y, t, in created_edge.discretization], [y for x, y, t, in created_edge.discretization], 'p-')
# plt.plot(x, y, 'p-')

prev_point = qI
si = 0
G = Tree()
root = G.add_vertex(numpy.array(qI))

for i, pt in enumerate(list_of_points):
    use_goal = qG is not None and i % 11 == 0
    
    if i%11 == 0:
        alpha = numpy.array(qG)
    else:
        alpha = list_of_points[si]
        si += 1
    
    ax.plot(alpha[0], alpha[1], 'g.')
    
    vn = G.get_nearest(alpha, distance_computator, 1e-3)
    qn = G.get_vertex_state(vn)
    (qs, edge) = stopping_configuration(
        qn, alpha, edge_creator, collision_checker, 1e-3
    )
    ax.plot(G.vertices[vn][0], G.vertices[vn][1], 'bo')
    print(f"The closes is claimed to be {G.vertices[vn]}")
    print(qs)
    
    if qs is None or edge is None:
        continue
    dist = distance_computator.get_distance(qn, qs)
    if dist > tol:
        vs = G.add_vertex(qs)
        G.add_edge(vn, vs, edge)
        if use_goal and distance_computator.get_distance(qs, qG) < tol:
            print("We Have Found the Goal")
            # return (G, root, vs)

    print("  ")

point_id = G.get_nearest(alpha, distance_computator, 1e-3)
point = G.get_vertex_state(point_id)
draw_edge, _ = dubins.path_sample(point, qG, 0.5, 0.1)
ax.plot(point[0], point[1], 'go')
ax.plot([x for x, y, z in draw_edge], [y for x, y, z in draw_edge], 'y-')

point, edge = stopping_configuration(point, qG, edge_creator, collision_checker, 1e-3)
draw_edge, _ = dubins.path_sample(point, qG, 0.5, 0.1)
ax.plot(point[0], point[1], 'go')
ax.plot([x for x, y, z in draw_edge], [y for x, y, z in draw_edge], 'y-')

# draw_edge, _ = dubins.path_sample(point, qG, 0.5, 0.1)
draw(ax, [(-4, 4), (-1.5, 1.5)], boundaries, qI, qG, G, [], "WHAT THE FUCK")

# p = dubins.shortest_path(qI, qG, 0.5)

# fig, ax = plt.subplots(1)

# ax.plot(qI[0], qI[1], marker = (3, 0, numpy.degrees(qI[2])))
# ax.plot(qG[0], qG[1], marker = (3, 0, numpy.degrees(qG[2])))

# # q, t = dubins.path_sample(qI, qG, 0.5, 0.1)
# q, t = p.sample_many(0.1)
# # for i in range(len(q)):
# #     print(f"{q[i]}   {t[i]}")

# q.append(qG)
# # t.append(p.path_length())

# # print(p.path_length())
# # print(len(t))
# # print(t)

# x = [states[0] for states in q]
# y = [states[1] for states in q]
# ax.plot(x + [qG[0]], y + [qG[1]], 'b-')
# # ax.plot(x, y, 'b-')

# random_state = (0.5, 1, 0)
# edge = DubinsEdge(qI, qG, p.path_length(), q, t, collision_checker = None, rho=0.5, step_size=0.01)
# point = edge.get_nearest_point(random_state)

# shortest_path, _ = dubins.path_sample(point[0], random_state, 0.5, 0.1)

# for states in shortest_path:
#     plt.plot(states[0], states[1], 'dk')

# plt.plot(point[0][0], point[0][1], 'ko' )
# plt.plot(random_state[0], random_state[1], marker = (3, 0, numpy.degrees(random_state[2])))


# # # print(p.path_length())

# # # print(edge.get_discretized_state(20))

# # # print(type(edge.split(2)))
# # # q, t = edge.split(2).sample_many(0.1)
# # # x = [states[0] for states in q]
# # # y = [states[1] for states in q]
# # # plt.plot(x, y, 'r-')
# # # print(edge.split(2))

plt.show()
