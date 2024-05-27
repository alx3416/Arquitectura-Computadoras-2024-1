set(TARGET_NAME my_new_Feature)

add_subdirectory(INIH)
set(sources my_new_Feature.cpp)
add_executable(${TARGET_NAME} ${sources})

target_link_libraries(${TARGET_NAME}
        PUBLIC
        INIH

)
