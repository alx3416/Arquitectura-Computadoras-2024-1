#include <iostream>

void arrayTest(int myNumbers[]){
    for (size_t i = 0; i < 5; i++) {
        myNumbers[i] = 7;
    }
}

int main()
{
    // Declaración de arreglos en C
    int myNumbers[] = {25, 50, 75, 100};
    std::cout << myNumbers[2] << std::endl;

    myNumbers[2] = 125;
    std::cout << myNumbers[2] << std::endl;

    // loop o bucle en un array
    for (size_t i = 0; i < 4; i++) {
        std::cout << "posición " << i << " su valor es " << myNumbers[i] << std::endl;
    }

    // Podemos crear array especificando tamaño
    int myArray[5];
    // Asignamos valores en un bucle o loop
    int value {10};
    for (size_t i = 0; i < 5; i++) {
        myArray[i] = value;
        std::cout << "posición " << i << " valor asignado de " << myArray[i] << std::endl;
        value += 10;
    }

    // Podemos imprimir la dirección de memoria de cada elemento
    for (size_t i = 0; i < 5; i++) {
        std::cout << "posición " << i << " su valor es " << myArray[i] <<
            " dirección memoria es " << &myArray[i] << std::endl;
    }

    // Tamaño de valor int
    int myInt {0};
    std::cout << "tamaño de int: " << sizeof(myInt) << std::endl;
    std::cout << "tamaño de Array int: " << sizeof(myArray) << std::endl;

    // En C, el nombre de un Array es en realidad un puntero al primer elemento
    // Obtengamos dirección de memoria de Array y del primer elemento
    std::cout << "dirección memoria Array: " << &myArray << std::endl;
    std::cout << "dirección memoria Array primer elemento: " << &myArray[0] << std::endl;

    // Si la variable del Array es sun puntero, entonces podemos obtener el valor con operador *
    std::cout << "Valor Array mediante puntero: " << *myArray << std::endl;

    for (size_t i = 0; i < 5; i++) {
        std::cout << "posición " << i << " su valor es " << *(myArray + i) <<
            " dirección memoria es " << &myArray[i] << std::endl;
    }

    // Podemos hacer un Array en 2D y tratarlo como una matriz
    int myMatrix[3][3] = {5};
    for (size_t rows = 0; rows < 3; rows++) {
        for (size_t cols = 0; cols < 3; cols++)
        {
            std::cout << myMatrix[rows][cols] << " ";
        }
        std::cout << std::endl;
    }

    arrayTest(myArray);

    // ¿Como hacer un programa que obtenga el determinante de una matriz de 2x2?

    // ¿Que pasa si quiero declarar una matriz de 2000x2000?
    // int myLargeMatrix[2000][2000];
    // ¿Como solucionarlo?
    return 0;

}
