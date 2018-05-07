ET(LIB_SRC hello.c)
ADD_DEFINITIONS("-DLIBHELLO_BUILD")
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)

#dynamic library
ADD_LIBRARY(libhello SHARED ${LIB_SRC})

set_target_properties(libhello PROPERTIES OUTPUT_NAME "hello")

install(TARGETS libhello DESTINATION /usr/lib)
install(FILES ${CMAKE_SOURCE_DIR}/libhello/hello.h DESTINATION /usr/include/hello)