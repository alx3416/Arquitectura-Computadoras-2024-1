#ifndef CPPBASICS_POINTERS_UTILS_H
#define CPPBASICS_POINTERS_UTILS_H

#include <chrono>
#include <iostream>
#include <vector>

namespace ptrs_basics {
    int squarePassByValue(int n) {
        n *= n;
        return n;
    }

    void squarePassByReference(int &n) {
        n *= n;
    }

    void squarePassByPointer(int *n_ptr) {
        int n = *n_ptr;
        n *= n;
        *n_ptr = n;
    }

    void swapByPointer(int *x, int *y){
        int z = *x;
        *x = *y;
        *y = z;
    }

    std::vector<int> fillVectorByValue(std::vector<int> vec){
        for(size_t i=0; i<vec.size(); i++){
            vec[i] = static_cast<int>(i);
        }
        return vec;
    }

    void fillVectorByReference(std::vector<int> &vec){
        for(size_t i=0; i<vec.size(); i++){
            vec[i] = static_cast<int>(i);
        }
    }
}  // ptrs_basics
#endif //CPPBASICS_POINTERS_UTILS_H
