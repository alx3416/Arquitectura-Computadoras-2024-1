#include <iostream>

void add_1D_arrays(int* result, const int* vectorA, const int* vectorB, int size){
    for (size_t i = 0; i < size; i++) {
        result[i] = vectorA[i] + vectorB[i];
    }
}

int main() {
    // Podemos crear array especificando tamaño
    int size = 10000000;
    int *vector1 = new int[size];
    int *vector2 = new int[size];
    int *vector3 = new int[size];
    // Asignamos valores en un bucle o loop

    for (size_t i = 0; i < size; i++) {
        vector1[i] = 1;
        vector2[i] = 2;
    }
    std::cout << "posicion 100 valor asignado de " << vector1[100] << std::endl;
    add_1D_arrays(vector3, vector1, vector2, size);
    std::cout << "posicion 100 valor asignado de " << vector3[100] << std::endl;
    std::cin.ignore(); // revisamos uso de RAM
    delete[] vector1;
    delete[] vector2;
    delete[] vector3;
    std::cin.ignore(); // revisamos uso de RAM
    return 0;

}
