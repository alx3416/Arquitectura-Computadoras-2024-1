#include <iostream>

int main() {
    int myAge = 43;
    int* ptr = &myAge;

    printf("%d\n", myAge);
    printf("%p\n", &myAge);
    printf("%p\n", ptr);

    char* myWord = "Hello";
    char myWord2[] = "Hello";

    printf("Second char is: %c\n", myWord[1]);
    printf("Second char is: %c\n", *(myWord+1));

    printf("Second char is: %s\n", (myWord+1));

    // Ahora declaremos una función para sumar dos números

    return 0;

}
