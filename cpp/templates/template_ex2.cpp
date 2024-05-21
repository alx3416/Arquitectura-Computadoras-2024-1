#include <iostream>

// Passing values as argument templates
template<typename data, int MIN, int MAX>
bool checkBoundaries(data x) {
    bool isSafe = false;
    if ((x < MAX) & (x > MIN)) {
        isSafe = true;
    }
    return isSafe;
}

int main() {
    // Call myMax for int
    std::cout << "check a number = ";
    int value{0};
    std::cin >> value;
    std::cout << checkBoundaries<int, -50, 50>(value) << std::endl;

    return 0;
}