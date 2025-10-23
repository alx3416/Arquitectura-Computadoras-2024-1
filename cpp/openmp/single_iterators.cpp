#include <iostream>
#include <omp.h>

int main()
{
    std::cout << "Sequential loop:" << std::endl;
    for (int i = 0; i <= 100; i++)
    {
        std::cout << " " << i << " ";
    }
    std::cout << std::endl << std::endl;

    std::cout << "Parallel loop with OpenMP:" << std::endl;

    // Set number of threads
    omp_set_num_threads(4);
    // omp_set_num_threads(omp_get_num_procs());
    std::cout << "Number of threads: " << omp_get_max_threads() << std::endl << std::endl;

#pragma omp parallel for
    for (int i = 0; i <= 100; i++)
    {
        std::cout << " " << i << " ";
    }
    std::cout << std::endl;

    return 0;
}