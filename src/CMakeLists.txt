include_directories(${PROJECT_SOURCE_DIR}/libhello)
SET(APP_SRC main.c)
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
ADD_EXECUTABLE(hello ${APP_SRC})

target_link_libraries(hello libhello)

install(TARGETS hello DESTINATION /usr/apps/com.mc.cmake_fei/bin)

