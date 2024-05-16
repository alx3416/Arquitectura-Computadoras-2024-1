set(SMART_POINTERS smart_pointers)
set(SMART_POINTERS_UNIQUE unique_pointers)
set(SMART_POINTERS_AUTO auto_pointers)

add_executable(${SMART_POINTERS} smart_pointers.cpp)
add_executable(${SMART_POINTERS_UNIQUE} unique_ptr_ex.cpp)
add_executable(${SMART_POINTERS_AUTO} auto_pointers_ex.cpp)