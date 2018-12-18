import graph_tool.all as gt

g = gt.Graph(directed=False)
v1 = g.add_vertex()
v2 = g.add_vertex()
e = g.add_edge(v1, v2)

g.save("graph.gt")
gl = gt.load_graph("graph.gt")
gl = gt.load_graph("mygraph.gt")
print(gl)
