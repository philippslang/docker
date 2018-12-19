import graph_tool.all as gt
import numpy as np
import sys

"""
g = gt.Graph(directed=False)
v1 = g.add_vertex()
v2 = g.add_vertex()
e = g.add_edge(v1, v2)

g.save("graph.gt")
"""

def normalize(a):
    c = a - a.min()
    if c.max() != 0.0:
        c /= c.max()
    return c

graph_name = "ixgraph"
nprop_viz, eprop_viz = "PORE_VOLUME_REFERENCE", "TRANSMISSIBILITY"
g = gt.load_graph("{}.gt".format(graph_name))
print(g)
g.list_properties()

nprop = g.vertex_properties[nprop_viz]
nprop.a = (normalize(nprop.a) + 1.0) * 10.0
eprop = g.edge_properties[eprop_viz]
eprop.a = normalize(eprop.a) + 1.0


#sys.exit()


gt.graph_draw(g, vertex_size=nprop, edge_color=eprop, edge_pen_width=eprop,
  output_size=(900, 800), bg_color=(1, 1, 1, 1), output="{}.png".format(graph_name))
