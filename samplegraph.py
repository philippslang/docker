import matplotlib
matplotlib.use('Agg')
import graph_tool.all as gt
import numpy as np
import sys
import time
import matplotlib.pyplot as plt


def normalize(a):
    c = a - a.min()
    if c.max() != 0.0:
        c /= c.max()
    return c

def run_step(name):
    def step_decorator(f):
        def timed_step(*args, **kwargs):
            start_time = time.time()
            print("starting {}...".format(name), end="")
            sys.stdout.flush()
            r = f(*args, **kwargs)
            print("finished {} in {:d}s.".format(name, int(time.time() - start_time)))
            return r
        return timed_step
    return step_decorator

@run_step("load")
def load(graph_name):
    return gt.load_graph("{}.gt".format(graph_name))

@run_step("layout")
def layout(g):
    return gt.sfdp_layout(g)

@run_step("render")
def render(g, eprop, nprop, graph_name, pos):
    gt.graph_draw(g, 
      # vertex_size=nprop, 
      # edge_pen_width=eprop,
      edge_color=eprop, 
      vertex_color=nprop,
      bg_color=(1, 1, 1, 1), 
      output="{}.png".format(graph_name),
      output_size=(900, 800), 
      pos=pos)

graph_name = "sugar_box_simple"
#graph_name = "OLYMPUS_1"
nprop_viz, eprop_viz = "PORE_VOLUME_REFERENCE", "TRANSMISSIBILITY"

g = load(graph_name)
print(g)
g.list_properties()

if 1:
    nb_bins = 10
    fig, axs = plt.subplots(1, 2, tight_layout=True)
    axs[0].hist(g.vertex_properties[nprop_viz].a, bins=nb_bins)
    axs[1].hist(g.edge_properties[eprop_viz].a, bins=nb_bins)
    plt.savefig("{}_histo.png".format(graph_name))

nprop = g.vertex_properties[nprop_viz]
nprop.a = (normalize(nprop.a) + 1.0) * 10.0
eprop = g.edge_properties[eprop_viz]
eprop.a = (normalize(eprop.a) + 1.0)**2

pos = layout(g)
render(g, eprop, nprop, graph_name, pos)
sys.exit()
u = gt.GraphView(g, efilt=lambda e: eprop[e] > eprop.a.max() / 2.0 )
gt.graph_draw(u, vertex_size=nprop, edge_color=eprop, edge_pen_width=eprop,
  output_size=(900, 800), bg_color=(1, 1, 1, 1), output="{}_filtered.png".format(graph_name),
  pos=pos)
