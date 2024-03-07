set(TARGET_NAME cpp_pointers)
set(TARGET_NAME_LEAK leak_memory)

add_executable(${TARGET_NAME} pointers.cpp
        pointers_utils.h)

add_executable(${TARGET_NAME_LEAK} leak_memory.cpp)