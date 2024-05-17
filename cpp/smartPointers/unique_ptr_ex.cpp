#include <iostream>
#include <memory>

class Rectangle {
    int length;
    int breadth;

public:
    Rectangle(int l, int b) {
        length = l;
        breadth = b;
    }

    void setLength(int l) {
        length = l;
    }

    int area() {
        return length * breadth;
    }
};

void setLenghtAndPrintArea(Rectangle myObject){
    myObject.setLength(100);
    std::cout << "New area is: " << myObject.area() << std::endl;
}

void setLenghtAndPrintAreaPtr(std::unique_ptr<Rectangle> & myObject){
    myObject->setLength(200);
    std::cout << "New area is: " << myObject->area() << std::endl;
}

int main() {
    auto newObject = Rectangle(7, 8);
    std::cout << newObject.area() << std::endl;
    std::unique_ptr<Rectangle> P1(new Rectangle(10, 5));
    std::cout << P1->area() << std::endl; // Aqui deben ser 50

    // std::unique_ptr<Rectangle> P2(nullptr);
    auto P2 = std::move(P1);


    // Aqui deben ser 50
    std::cout << P2->area() << std::endl;

    // Esta linea crashea el programa
    // std::cout << P1->area() << std::endl;

    // ¿Podemos pasar como argumentos de entrada los punteros unique a una función?
    // Sin puntero inteligente
    setLenghtAndPrintArea(newObject);
    std::cout << newObject.area() << std::endl;
    setLenghtAndPrintAreaPtr(P2);
    std::cout << P2->area() << std::endl;


    return 0;
}