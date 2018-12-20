import common

import graph_tool.all as gt
import numpy as np
import sys
import time
import pickle


start_time = time.time()

graph_name = "dbg"
nprop_viz, eprop_viz = "POROSITY", "TRANSMISSIBILITY"

g = common.load(graph_name)
print(g)
g.list_properties()

pos_fname = "pos.pk"
idx = [0, 1]
if 0:
    pos = common.layout(g)
    pos_data = pos.get_2d_array(idx)
    with open(pos_fname, "wb") as f:
        pickle.dump(pos_data, f)
else:
    with open(pos_fname, "rb") as f:
        pos_data = pickle.load(f)
    pos = g.new_vertex_property("vector<double>")
    pos.set_2d_array(pos_data, idx)


idx = [0, 1]
pos_array = pos.get_2d_array(idx)
posx = pos_array[0]
posy = pos_array[1]
print(len(posy))
xmin, xmax = np.amin(posx), np.amax(posx)
ymin, ymax = np.amin(posy), np.amax(posy)
xspan = xmax - xmin
yspan = ymax - ymin
span = max(xspan, yspan)
print(xmin, xmax, xspan)
print(ymin, ymax, yspan)
span = span * 1.2

"""
      |
      |
------|------ + x
      |
      |    min(x,y)
     + y     --------
            |        | W
            |        |
             -------- max(x,y)
                H
"""

fit_view = (xmin, ymin, span, span)

nprop = g.vertex_properties[nprop_viz]
eprop = g.edge_properties[eprop_viz]
pos = common.render(g, eprop, nprop, graph_name, pos, 5, fit_view=fit_view)

poromax = np.amax(nprop.ma)
cutoff = 0.8
poromin_filter = poromax * cutoff
u = common.view(g, vfilter=lambda e: nprop[e] > poromin_filter)
nprop = u.vertex_properties[nprop_viz]
eprop = u.edge_properties[eprop_viz]
print(u)
common.render(u, eprop, nprop, graph_name + "view1", pos, 5, fit_view=fit_view)


print("all done in {:d}s".format(int(time.time() - start_time)))
