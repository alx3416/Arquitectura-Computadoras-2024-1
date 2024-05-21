set(TARGET_NAME cpp_pointers)
set(TARGET_NAME_ARRAYS cpp_pointers_arrays)
set(TARGET_NAME_POINTERS cpp_pointers_basics)
set(TARGET_NAME_LEAK leak_memory)
set(TARGET_NAME_HEAP heap_allocating)
set(TARGET_NAME_HEAP_CPP heap_allocating_new)
set(TARGET_NAME_BUBBLE bubble_sort)
set(TARGET_NAME_MULTIPLY array_multiply)

add_executable(${TARGET_NAME} pointers.cpp
        pointers_utils.h)

add_executable(${TARGET_NAME_LEAK} leak_memory.cpp)

add_executable(${TARGET_NAME_POINTERS} pointers_basics.cpp)

add_executable(${TARGET_NAME_ARRAYS} pointers_arrays.cpp)

add_executable(${TARGET_NAME_HEAP} heap_allocating.cpp)

add_executable(${TARGET_NAME_HEAP_CPP} heap_allocating_new.cpp)

add_executable(${TARGET_NAME_BUBBLE} main_sort.cpp)

add_executable(${TARGET_NAME_MULTIPLY} main_multiply.cpp)