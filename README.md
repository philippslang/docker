```
docker run -it --rm -v $(pwd):/out tiagopeixoto/graph-tool /bin/bash
hexdump graph.gt -C
hexdump mygraph.gt -C
g++ -Wall graphml.cpp
./a.out
python samplegraph.py
```
