#include <iostream>
#include <cstdlib>

// multiply matrices function with dynamic memory
void multiplyMatrices() {
    // we need to create an algo to multiply matrices!
    ;
}

// Function to print an array
void print2DArray(int **array, int const rows, int const columns) {
    std::cout << "Printing array: " << std::endl;
    for (size_t i = 0; i < rows; i++) {
        for (size_t j = 0; j < columns; j++) {
            std::cout << " " << array[i][j];
        }
        std::cout << std::endl;
    }
}

void set2DArray(int **array, int const rows, int const columns) {
    int value = 0;
    for (size_t i = 0; i < rows; i++) {
        for (size_t j = 0; j < columns; j++) {
            array[i][j] = value;
        }
        value += 1;
    }
}

// Driver program to test above functions
int main() {
    // you can try other sizes
    int rows = 5;
    int columns = 7;
    int **matrix = new int *[rows];
    for (int i = 0; i < rows; ++i) {
        matrix[i] = new int[columns];
    }

    /* Declare 2 matrices that comply the condition
     -  The number of columns of the 1st matrix must equal
        the number of rows of the 2nd matrix.
     -  The result will have the same number of rows as the 1st matrix
        and the same number of columns as the 2nd matrix.
     */

    std::cout << "print arrays : \n";
    // set values and print both matrices
    set2DArray(matrix, rows, columns);
    print2DArray(matrix, rows, columns);

    // multiply matrices
    multiplyMatrices();

    // print the result!


    // this code is to deallocate memory
    for (int i = 0; i < rows; ++i) {
        delete[] matrix[i];
    }
    delete[] matrix;

    return 0;
}