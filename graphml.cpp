#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>


template<typename T>
void writebytes(std::ofstream& gtfile, const T& v)
{
    gtfile.write(reinterpret_cast<const char*>(&v),
      sizeof(v));
}

void writebytes(std::ofstream& gtfile, const std::string& v)
{
    const uint64_t size = v.size();
    writebytes(gtfile, size);
    for (auto c : v)
    {
        gtfile << char(c);
    }
}
 
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
        const std::string comment = "undirected test graph file with two vertices, one edge and no properties";
        writebytes(gtfile, comment);

        // undirected
        gtfile << char(false);

        // adjacency
        const uint64_t nnodes = 2;
        writebytes(gtfile, nnodes);        
        const uint64_t nedgesnode0 = 1;
        writebytes(gtfile, nedgesnode0);        
        const uint8_t outnodeedge0 = 1;
        writebytes(gtfile, outnodeedge0);        
        const uint64_t nedgesnode1 = 0;
        writebytes(gtfile, nedgesnode1);

        // prop maps
        const uint64_t npropmaps = 2;
        writebytes(gtfile, npropmaps);
        
        // node prop, double
        {
            const uint8_t proploc = 1;
            writebytes(gtfile, proploc);
            const std::string propname = "poro";
            writebytes(gtfile, propname);
            const uint8_t proptype = 4;
            writebytes(gtfile, proptype);
            const double val0 = 1.5;
            writebytes(gtfile, val0);
            const double val1 = 2.5;
            writebytes(gtfile, val1);
        }
        // edge prop, double
        {
            const uint8_t proploc = 2;
            writebytes(gtfile, proploc);
            const std::string propname = "trans";
            writebytes(gtfile, propname);
            const uint8_t proptype = 4;
            writebytes(gtfile, proptype);
            const double val0 = 3.5;
            writebytes(gtfile, val0);
        }
        gtfile.close();
    }
    return 0;
}
