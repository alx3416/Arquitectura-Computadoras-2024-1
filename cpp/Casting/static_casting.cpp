#include <iostream>

// We use static_cast for standard type conversions,
// such as converting from float to int.
int main() {
    float my_float = 3.14;

    // convert float to int
    int my_int = static_cast<int>(my_float);
    std::cout << "Float: " << my_float << " -> Int: " << my_int << std::endl;

    return 0;
}