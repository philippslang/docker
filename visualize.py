import common

import graph_tool.all as gt
import numpy as np
import sys
import time



start_time = time.time()

graph_name = "dbg"
nprop_viz, eprop_viz = "POROSITY", "TRANSMISSIBILITY"

g = common.load(graph_name)
print(g)
g.list_properties()

pos = common.layout(g)


idx = [0, 1, 2]
pos_array = pos.get_2d_array(idx)
posx = pos_array[0]
posy = pos_array[1]
xmin, xmax = np.amin(posx), np.amax(posx)
ymin, ymax = np.amin(posy), np.amax(posy)
xspan = xmax - xmin
yspan = ymax - ymin
print(xmin, xmax, xspan)
print(ymin, ymax, yspan)
fit_view = (-10, 0, 100, 100) # (xmin, ymin, xspan, yspan) # 1.0 #True # (0, 0, 8, 8)
print(fit_view)

nprop = g.vertex_properties[nprop_viz]
eprop = g.edge_properties[eprop_viz]
pos = common.render(g, eprop, nprop, graph_name, pos, 5, fit_view=fit_view)

print("all done in {:d}s".format(int(time.time() - start_time)))
