#include <iostream>


int main()
{
    std::cout << "idea general sobre auto_ptr (no disponible desde C++17)" << std::endl;
    int *i = new int;
    std::auto_ptr<int> x(i);
    std::auto_ptr<int> y(nullptr);

    // y = x;
    y = std::move(x);

    std::cout << "auto_ptr x = " << x.get() << std::endl; // Print NULL
    std::cout << "auto_ptr y = " << y.get() << std::endl; // Print non-NULL address i
}
