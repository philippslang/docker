import matplotlib
matplotlib.use('cairo')
import graph_tool.all as gt
import numpy as np
import sys
import time
import matplotlib.pyplot as plt
import graph_tool.draw as gtd

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
            print("finished in {:d}s.".format(int(time.time() - start_time)))
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
def render(g, eprop, nprop, graph_name, pos, vertex_size=None, 
  edge_pen_width=None, **kwargs):
    _graph_draw = gt.graph_draw
    pos = _graph_draw(g, 
      vertex_size=vertex_size, 
      edge_pen_width=edge_pen_width,
      edge_color=eprop, 
      vertex_color=nprop,
      vertex_fill_color=nprop,
      bg_color=(1, 1, 1, 1), 
      output="{}.png".format(graph_name),
      #output_size=(900, 800), 
      pos=pos,
      vcmap=matplotlib.cm.plasma,
      **kwargs)
    return pos

@run_step("histograms")
def histo(props, graph_name, nb_bins=10):    
    fig, axs = plt.subplots(1, len(props), tight_layout=True)
    for (name, prop), ax in zip(props, axs):
        ax.hist(prop.ma, bins=nb_bins)
        ax.set_title(name)
    plt.savefig("{}_histos.png".format(graph_name))

@run_step("constructing view")
def view(g, vfilter=None, efilter=None):    
    return gt.GraphView(g, vfilt=vfilter, efilt=efilter)

