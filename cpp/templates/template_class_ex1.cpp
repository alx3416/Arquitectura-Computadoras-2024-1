#include <iostream>


// Class template
template<class T>
class Number {
private:
    // Variable of type T
    T num;

public:

    explicit Number(T n) : num(n) {}   // constructor

    T getNum() {
        return num;
    }

    // Function prototype
    void setNum(T value);
};

// Function definition
template<class T>
void Number<T>::setNum(T const value) {
    num = value;
}

int main() {

    // create object with int type
    Number<int> numberInt(7);

    // create object with double type
    Number<double> numberDouble(7.7);

    std::cout << "int Number = " << numberInt.getNum() << std::endl;
    std::cout << "double Number = " << numberDouble.getNum() << std::endl;

    std::cout << "save a number = ";
    int value {0};
    std::cin >> value;
    numberInt.setNum(value);
    std::cout << "int Number = " << numberInt.getNum() << std::endl;


    return 0;
}