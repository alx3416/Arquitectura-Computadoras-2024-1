#include <iostream>
#include "pointers_utils.h"

int main() {


    std::string food = "Pizza"; // A food variable of type string

    std::cout << food << "\n";  // Outputs the value of food (Pizza)
    std::cout << &food << "\n"; // Outputs the memory address of food (0x6dfed4)

    std::string *food_ptr = &food;    // A pointer variable, with the name ptr, that stores the address of food

    // Output the memory address of food with the pointer (0x6dfed4)
    std::cout << food_ptr << "\n";
    // Output the value of food from pointer
    std::cout << *food_ptr << "\n";

    // new and delete operators
    // pointer-variable = new data-type(value);
    // int *p = nullptr;
    // p = new int;
    // option 2
    // int *r = new int;
    int* p = new int(25);
    std::cout << "p Address: " << p << std::endl;
    std::cout << "p value: " << *p << std::endl;
    delete p;


    std::cout << "Press any key to continue\n";
    std::cin.ignore();
    // trying with a very large c-array
    int myArray[5] = {10, 20, 30, 40, 50};
    int length = 50000000;
    int *pArray = new int[length];
    for(int i = 0; i < length; i++ ){
        pArray[i] = i;
    }
    /*
    for(int i = 0; i < length; i++ ){
        std::cout << pArray[i] << std::endl;
    }
    */

    std::cout << "Press any key to exit\n";
    std::cin.ignore();
    delete[] pArray;

    return 0;

}
