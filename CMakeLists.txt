cmake_minimum_required(VERSION 3.16)

set(CMAKE_TOOLCHAIN_FILE ${CMAKE_CURRENT_SOURCE_DIR}/vcpkg/scripts/buildsystems/vcpkg.cmake CACHE STRING "Vcpkg toolchain file")

project(python-filerix VERSION 1.1.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(GNUInstallDirs)

include_directories(${CMAKE_SOURCE_DIR}/include)

find_package(filerix CONFIG REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(python_filerix src/pybind11.cc)

set_target_properties(python_filerix PROPERTIES OUTPUT_NAME "filerix")

target_link_libraries(python_filerix PRIVATE 
  filerix::filerix
)

install(TARGETS python_filerix
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages
)
