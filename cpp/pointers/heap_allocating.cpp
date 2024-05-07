#include <iostream>
#include <cstdlib>

// check https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/

int main()
{
    // C malloc()
    // memory allocation, regresa un puntero del tipo void, que puede ser casteado a otro tipo de dato
    int* ptrLargeArray = (int*)malloc(4000000 * sizeof(int));

    // ejemplo usando dos instrucciones en lugar de una
    void* ptr = malloc(4000000 * sizeof(int));
    auto ptr_int = (int*)ptr;

    // Podemos usar C++ casting
    auto ptrLargeArray2 = static_cast<int*>(malloc(4000000 * sizeof(int)));

    std::cout << "position 123,456: " << ptrLargeArray[123456] << " valor al crear arreglo \n";
    for (size_t j = 0; j < 4000000; j++)
    {
        ptrLargeArray[j] = 7;
    }

    std::cout << "position 123,456: " << ptrLargeArray[123456] << " Press any key to continue \n";
    std::cin.ignore(); // revisamos uso de RAM

    // Es responsabilidad del desarrollador liberar memoria después de usarse
    free(ptrLargeArray);
    free(ptr_int);

    // C calloc
    // contiguous allocation, la diferencia es que los valores del arreglo por default son cero al inicio
    // se pasan dos argumentos de entrada, numero de elementos  y su tamaño

    auto myArray = (int*)calloc(4000000, sizeof(int));

    std::cout << "position 123,456: " << myArray[123456] << " valor al crear arreglo \n";
    for (size_t j = 0; j < 4000000; j++)
    {
        myArray[j] = 121212;
    }

    std::cout << "position 123,456: " << myArray[123456] << " Press any key to continue \n";
    std::cin.ignore(); // revisamos uso de RAM

    // C realloc
    // modifica el tamaño del array, en caso de añadir valores, estos se inician en cero
    auto mySmallArray = (int*)realloc(myArray, 10 * sizeof(int));
    for (size_t j = 0; j < 10; j++)
    {
        mySmallArray[j] = 3;
    }
    for (size_t j = 0; j < 10; j++)
    {
        std::cout << "position " << j << " valor guardado es " << mySmallArray[j] << std::endl;
    }
    free(mySmallArray);


    return 0;
}
