import common

import graph_tool.all as gt
import numpy as np
import sys
import time



start_time = time.time()

graph_name = "sugar_box_simple"
graph_name = "OLYMPUS_1"
nprop_viz, eprop_viz = "POROSITY", "TRANSMISSIBILITY"

g = common.load(graph_name)
print(g)
g.list_properties()

nprop = g.vertex_properties[nprop_viz]
eprop = g.edge_properties[eprop_viz]
common.histo([(nprop_viz, nprop), (eprop_viz, eprop)], graph_name)

eprop.a = common.normalize(eprop.a)
common.histo([(nprop_viz, nprop), (eprop_viz, eprop)], graph_name + "_norm")

xcoords = g.vertex_properties["CELL_CENTER_X"]
ycoords = g.vertex_properties["CELL_CENTER_Y"]
xmin, xmax = np.amin(xcoords.a), np.amax(xcoords.a)
ymin, ymax = np.amin(ycoords.a), np.amax(ycoords.a)
deltax = xmax - xmin
deltay = ymax - ymin
reduction_factor = 0.1
ymax_filter = ymin + reduction_factor * deltay
xmax_filter = xmin + reduction_factor * deltax
u = common.view(g, vfilter=lambda e: xcoords[e] < xmax_filter)
u = common.view(u, vfilter=lambda e: ycoords[e] < ymax_filter)

u.save("dbg.gt")
sys.exit()

pos = common.layout(u)
pos_array = pos.get_2d_array([0, 1])
print(pos_array.size)
print(pos_array)
print(pos_array[0])
print(pos_array[1])
print(np.amax(pos_array[0]), np.amin(pos_array[0]))
print(np.amax(pos_array[1]), np.amin(pos_array[1]))
fit_view = (0, 1, 90, 120) # 1.0 #True # (0, 0, 8, 8)

nprop = u.vertex_properties[nprop_viz]
eprop = u.edge_properties[eprop_viz]
print(u)
common.histo([(nprop_viz, nprop), (eprop_viz, eprop)], graph_name + "_norm_view0")
pos = common.render(u, eprop, nprop, graph_name + "view0", pos, 5, fit_view=fit_view)

sys.exit()

poromax = np.amax(nprop.ma)
cutoff = 0.8
poromin_filter = poromax * cutoff
u = common.view(u, vfilter=lambda e: nprop[e] > poromin_filter)
nprop = u.vertex_properties[nprop_viz]
eprop = u.edge_properties[eprop_viz]
print(u)
common.histo([(nprop_viz, nprop), (eprop_viz, eprop)], graph_name + "_norm_view1")
common.render(u, eprop, nprop, graph_name + "view1", pos, 5, fit_view=fit_view)


print("all done in {:d}s".format(int(time.time() - start_time)))
