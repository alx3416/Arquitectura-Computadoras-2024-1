#include <iostream>

class SmartPtr {
    int* ptr; // Puntero a almacenar
public:
    // Constructor
    explicit SmartPtr(int* p = nullptr) {
    ptr = p;
    }

    // Destructor
    ~SmartPtr() {
    delete (ptr);
    }

    // Overloading operator derreferencia
    int& operator*() {
    return *ptr;
    }
};

int main()
{
    SmartPtr ptr(new int());
    *ptr = 20;
    std::cout << *ptr;

    // We don't need to call delete ptr: when the object
    // ptr goes out of scope, the destructor for it is
    // automatically called and destructor does delete ptr.

    return 0;
}
