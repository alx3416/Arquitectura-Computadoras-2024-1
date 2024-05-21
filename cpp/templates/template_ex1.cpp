#include <iostream>

// One function works for all data types
template <typename data>
data myMax(data x, data y)
{
    return (x > y) ? x : y;
}

int main()
{
    // Call myMax for int
    std::cout << myMax<int>(3, 7) << std::endl;
    // call myMax for double
    std::cout << myMax<double>(3.0, 7.0) << std::endl;
    // call myMax for char
    std::cout << myMax<char>('g', 'e') << std::endl;

    return 0;
}