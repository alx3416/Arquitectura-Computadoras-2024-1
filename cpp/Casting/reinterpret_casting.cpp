#include <iostream>

// reinterpret_cast is used to convert one pointer type
// to another pointer type or one reference type to
// another reference type.
//
//Unlike static_cast, reinterpret_cast doesn't actually
// convert the data types but reinterprets one pointer
// type as another at compile time.
int main() {
    // create an integer variable
    int x = 67;

    // pointer to an integer
    int *ptr_to_int = &x;

    // reinterpret the pointer to an integer
    // as a pointer to char
    char *ptr_to_char = reinterpret_cast<char *>(ptr_to_int);

    // dereference the double pointer
    // originally holding an integer as if it contains a double
    std::cout << "Dereferencing ptr_to_char: " << *ptr_to_char << std::endl;

    return 0;
}