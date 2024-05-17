//
// By using shared_ptr more than one pointer
// can point to this one object at a time and
// it’ll maintain a Reference Counter using
// the use_count()
//
#include <iostream>
// Dynamic Memory management library
#include <memory>

class Square {
    int length;
    int breadth;

public:
    Square(int l, int b)
    {
        length = l;
        breadth = b;
    }

    int area() { return length * breadth; }
};

int main()
{
    //---\/ Smart Pointer
    std::shared_ptr<Square> P1(new Square(10, 5));
    // This'll print 50
    std::cout << P1->area() << std::endl;

    std::shared_ptr<Square> P2;
    P2 = P1;

    // This'll print 50
    std::cout << P2->area() << std::endl;

    // This'll now not give an error,
    std::cout << P1->area() << std::endl;

    // This'll also print 50 now
    // This'll print 2 as Reference Counter is 2
    std::cout << P1.use_count() << std::endl;
    std::cout << P2.use_count() << std::endl;
    return 0;
}