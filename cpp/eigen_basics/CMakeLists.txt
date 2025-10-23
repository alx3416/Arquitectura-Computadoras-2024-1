find_package(Eigen3 REQUIRED)

set(EIGEN_EX1 eigen_ex1)
include_directories(${Eigen3_INCLUDE_DIRS})

add_executable(${EIGEN_EX1} hello_world_eigen.cpp)

target_link_libraries(${EIGEN_EX1}
        PRIVATE
        Eigen3::Eigen)
