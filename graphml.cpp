#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
 
int main() {
    std::ofstream gtfile("mygraph.gt", std::ios::binary);

    if(gtfile.is_open())
    { 
        // header
        gtfile << char(0xe2) << char(0x9b);
        gtfile << char(0xbe) << char(0x20);
        gtfile << char(0x67) << char(0x74);
        gtfile << char(0x01) << char(0x00);

        // comment
        std::string comment = "test graph file with two vertices";
        const uint64_t comment_size = comment.size();
        gtfile.write(reinterpret_cast<const char*>(&comment_size),
          sizeof(comment_size));
        for (auto c : comment)
        {
           gtfile << char(c);
        }

        // undirected
        gtfile << char(false);

        const uint64_t nnodes = 2;
        gtfile.write(reinterpret_cast<const char*>(&nnodes),
          sizeof(nnodes));
        
        const uint64_t nedgesnode0 = 1;
        gtfile.write(reinterpret_cast<const char*>(&nedgesnode0),
          sizeof(nedgesnode0));
        
        const uint8_t outnodeedge0 = 1;
        gtfile.write(reinterpret_cast<const char*>(&outnodeedge0),
          sizeof(outnodeedge0));
        
        const uint64_t nedgesnode1 = 0;
        gtfile.write(reinterpret_cast<const char*>(&nedgesnode1),
          sizeof(nedgesnode1));

        const uint64_t npropmaps = 0;
        gtfile.write(reinterpret_cast<const char*>(&npropmaps),
          sizeof(npropmaps));

        gtfile.close();
    }
    return 0;
}
