# Find OpenMP
find_package(OpenMP REQUIRED)

# Create executable
add_executable(openmp_test single_iterators.cpp)
add_executable(openmp_test_2 single_vs_multiple.cpp)

# Link OpenMP
target_link_libraries(openmp_test OpenMP::OpenMP_CXX)
target_link_libraries(openmp_test_2 OpenMP::OpenMP_CXX)