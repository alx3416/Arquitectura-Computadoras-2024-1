
find_package(OpenMP REQUIRED)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
# added -fopenmp
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -fopenmp")

set(TARGET_NAME cpp_openmp)

add_executable(${TARGET_NAME}
        parallel_examples.cpp
        parallel_utils.h
)

if (MSVC)
    set_target_properties(${TARGET_NAME} PROPERTIES LINK_FLAGS /STACK:2000000000)
endif (MSVC)

target_link_libraries(cpp_openmp OpenMP::OpenMP_CXX)