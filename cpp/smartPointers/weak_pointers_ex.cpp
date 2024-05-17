//
// Weak_ptr is a smart pointer that holds a non-owning
// reference to an object. It’s much more similar to
// shared_ptr except it’ll not maintain a
// Reference Counter. In this case, a pointer will not
// have a stronghold on the object. The reason is
// if suppose pointers are holding the object and
// requesting for other objects then they may form a Deadlock.
//

#include <iostream>
// Dynamic Memory management library
#include <memory>

class TriangleRectangle {
    float length;
    float breadth;

public:
    TriangleRectangle(float l, float b) {
        length = l;
        breadth = b;
    }

    float area() { return (length * breadth) / 2.0; }
};

int main() {
    //---\/ Smart Pointer
    std::shared_ptr<TriangleRectangle> P1(new TriangleRectangle(10, 5));

    // create weak ptr
    std::weak_ptr<TriangleRectangle> P2(P1);

    // This'll print 50
    std::cout << P1->area() << std::endl;

    // This'll print 1 as Reference Counter is 1
    std::cout << P1.use_count() << std::endl;
    return 0;
}

// what problem arise with shared pointers?
// circle reference:
// class A { shared_ptr<B> b; ... };
// class B { shared_ptr<A> a; ... };
// shared_ptr<A> x(new A);  // +1
// x->b = new B;            // +1
// The reference count is 2, so we can't delete any pointer
// shared pointer only can be deleted when count = 0;