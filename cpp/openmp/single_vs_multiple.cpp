#include <iostream>
#include <omp.h>
#include <chrono>

int main()
{
    const int iterations = 1000000;
    long long sum_sequential = 0;
    long long sum_parallel = 0;

    // Set number of threads for parallel execution
    omp_set_num_threads(4);
    std::cout << "Number of threads: " << omp_get_max_threads() << std::endl << std::endl;

    // Sequential execution
    std::cout << "Sequential loop:" << std::endl;
    auto start_seq = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < iterations; i++)
    {
        // sum_sequential++;
        sum_sequential  += i;
    }

    auto end_seq = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_seq = end_seq - start_seq;

    std::cout << "Sum: " << sum_sequential << std::endl;
    std::cout << "Time: " << elapsed_seq.count() << " seconds" << std::endl << std::endl;

    // Parallel execution with OpenMP
    std::cout << "Parallel loop with OpenMP:" << std::endl;
    auto start_par = std::chrono::high_resolution_clock::now();

#pragma omp parallel for reduction(+:sum_parallel)
    for (int i = 0; i < iterations; i++)
    {
        //sum parallel++;
        sum_parallel += i;
    }

    auto end_par = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_par = end_par - start_par;

    std::cout << "Sum: " << sum_parallel << std::endl;
    std::cout << "Time: " << elapsed_par.count() << " seconds" << std::endl << std::endl;

    // Speedup calculation
    double speedup = elapsed_seq.count() / elapsed_par.count();
    std::cout << "Speedup: " << speedup << "x" << std::endl;

    return 0;
}