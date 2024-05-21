#include <iostream>
#include <stdio.h>

int addValues(int a, int b){
    a = 0;
    return a + b;
}

void addValues2(int &res,const int &a, const int &b){
    res = a + b;
}

void swapValues(int* x, int* y){
    int z = *x;
    *x = *y;
    *y = z;
}
// vector<int> vect(n, 10);
// vector<int> vect{ 10, 20, 30 };
// vector<int> vect1(10);

int main() {
    int myAge = 43;
    int* ptr = &myAge;

    printf("%d\n", myAge);
    printf("%p\n", &myAge);
    printf("%d\n", *ptr);

    char* myWord = "Hello";

    printf("Second char is: %c\n", myWord[1]);
    printf("Second char is: %c\n", *(myWord+1));

    printf("Second char is: %s\n", (myWord+1));

    // Ahora declaremos una función para sumar dos números
    int a{7};
    int b{8};
    int c{0};
    c = addValues(a, b);
    addValues2(c, a, b);
    int value1{100};
    int value2{-99};
    int* ptr1 = nullptr;
    std::cout << "valor 1: " << value1 << std::endl;
    std::cout << "valor 2: " << value2 << std::endl;
    swapValues(ptr1, &value2);
    std::cout << "After swap\n";
    std::cout << "valor 1: " << value1 << std::endl;
    std::cout << "valor 2: " << value2 << std::endl;
    return 0;
    auto x = std::scanf();
}
