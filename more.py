import common

import graph_tool.all as gt
import numpy as np
import sys
import time
import pickle


start_time = time.time()

graph_name = "zbug"

g = gt.Graph(directed=False)
v1 = g.add_vertex()
v2 = g.add_vertex()
e = g.add_edge(v1, v2)

idx = [0, 1]
pos = common.layout(g)
pos_data = pos.get_2d_array(idx)
print(pos_data)
#pos_data[1][1] = 0.5 # [yaxis][node1]
pos_data[0][0] = 0.5 # [yaxis][node1]
pos.set_2d_array(pos_data, idx)
pos_data = pos.get_2d_array(idx)
print(pos_data)
pos = common.render(g, None, None, graph_name, pos, vertex_text=g.vertex_index, vertex_font_size=18)
