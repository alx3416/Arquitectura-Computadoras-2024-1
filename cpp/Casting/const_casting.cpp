#include <iostream>

// We use const_cast to cast away the const qualifier from a variable.
//
//One common scenario where we can use const_cast is when
// working with third-party libraries that have functions
// which take non-const pointers as arguments,
// but we need to pass in const data.

// function that takes a non-const pointer
void modify_data(int *data) {
    // modify the data
    *data *= 2;
}

int main() {
    int x = 10;

    // a const pointer for variable x
    const int *ptr = &x;

    // use const_cast to
    // remove const qualifier and allow modification
    int *mutable_ptr = const_cast<int *>(ptr);

    // call the function
    modify_data(mutable_ptr);

    // value is modified successfully
    std::cout << "Modified value: " << x << std::endl;

    return 0;
}