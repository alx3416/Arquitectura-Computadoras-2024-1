#include <iostream>
#include <stdlib.h>

// check https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/

int main()
{
    //  C++ dynamic memory
    //  Para usar HEAP usamos new, para borrar, delete
    size_t n = 10;
    int *data = new int[n];

    for (size_t j = 0; j < 10; j++)
    {
        std::cout << "position " << j << " valor guardado es " << data[j] << std::endl;
    }

    for (size_t j = 0; j < n; j++)
    {
        data[j] = 11;
    }

    std::cout << "position " << 3 << " valor guardado es " << data[3] << std::endl;
    std::cin.ignore(); // revisamos uso de RAM

    delete[] data;

    return 0;
}
