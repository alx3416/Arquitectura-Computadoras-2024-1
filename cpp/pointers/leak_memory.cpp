#include <iostream>

class SampleClass {
private:
    int value;
};

void fun()
{
    SampleClass* p = new SampleClass();
}

int main()
{
    // No delete used, memory usage will increment until a crash
    while (1) {
        fun();
    }
}