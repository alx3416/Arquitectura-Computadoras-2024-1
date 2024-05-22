#include <iostream>

// We mainly use dynamic_cast for polymorphic type conversions,
// especially when dealing with inheritance hierarchies.
// It's typically used in scenarios where a base class pointer
// needs to be converted to a derived class pointer
class Base {
public:
    // base class print function
    virtual void print() {
        std::cout << "Base class" << std::endl;
    }
};

class Derived : public Base {
public:
    // derived class print function overriding the base class
    void print() override {
        std::cout << "Derived class" << std::endl;
    }
};

int main() {
    // create a Base class pointer
    // pointing to a Derived object
    Base *base_ptr = new Derived();

    base_ptr->print();

    // use dynamic_cast to cast the
    // Base pointer to a Derived pointer
    Derived *derived_ptr = dynamic_cast<Derived *>(base_ptr);

    // call the print function through the derived pointer
    if (derived_ptr) {
        derived_ptr->print();
    }

    // delete the dynamically allocated object
    delete base_ptr;

    return 0;
}