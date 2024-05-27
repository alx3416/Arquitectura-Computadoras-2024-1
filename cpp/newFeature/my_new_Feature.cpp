#include <iostream>
#include "INIH/INIReader.h"

int main(int argc, char* argv[]) {
    if (argc <= 1) {
        std::cout << "Hello World! no arguments passed\n";
        return 0;
    }
    INIReader initial_cfg(argv[1]);
    if (initial_cfg.ParseError() < 0) {
        std::cout << "Can't load config ini file'\n";
        return 0;
    }

    auto const value1 = initial_cfg.GetInteger("VALUES", "first_variable", 111);
    auto const value2 = initial_cfg.GetReal("VALUES", "second_variable", 222.333);
    std::cout << "Hello World! first value: " << value1 << " second value: " << value2 << std::endl;

    return 1;
}