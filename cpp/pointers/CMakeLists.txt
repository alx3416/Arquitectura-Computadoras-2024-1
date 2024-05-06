set(TARGET_NAME cpp_pointers)
set(TARGET_NAME_ARRAYS cpp_pointers_arrays)
set(TARGET_NAME_POINTERS cpp_pointers_basics)
set(TARGET_NAME_LEAK leak_memory)

add_executable(${TARGET_NAME} pointers.cpp
        pointers_utils.h)

add_executable(${TARGET_NAME_LEAK} leak_memory.cpp)

add_executable(${TARGET_NAME_POINTERS} pointers_basics.cpp)

add_executable(${TARGET_NAME_ARRAYS} pointers_arrays.cpp)