#include <iostream>

int main() {
    // assigning an int value to num_int
    int num_int = 9;

    // declaring a double type variable
    double num_double;

    // implicit conversion
    // assigning int value to a double variable
    num_double = num_int;

    std::cout << "num_int = " << num_int << std::endl;
    std::cout << "num_double = " << num_double << std::endl;

    return 0;
}