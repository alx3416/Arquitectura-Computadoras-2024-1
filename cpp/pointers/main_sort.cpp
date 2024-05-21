#include <iostream>
#include <cstdlib>

// Bubble sort function
void bubbleSort(int arr[], int const n){
    // we need to create an algo to sort a vector!
}

// Function to print an array
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        std::cout << " " << arr[i];
}

// Driver program to test above functions
int main()
{
    int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
    int N = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, N);
    std::cout << "Sorted array: \n";
    printArray(arr, N);
    return 0;
}