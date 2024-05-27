
add_library (INIH
        ini.c
        ini.h
        INIReader.h
        INIReader.cpp)

target_include_directories (INIH PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})