```
docker run -it --rm -v $(pwd):/out tiagopeixoto/graph-tool /bin/bash
hexdump graph.gt -C
hexdump sugar_box_simple.gt -C
g++ -Wall graphml.cpp
./a.out
python samplegraph.py
```
