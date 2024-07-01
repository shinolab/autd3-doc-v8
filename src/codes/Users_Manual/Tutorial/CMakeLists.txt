cmake_minimum_required(VERSION 3.21)

project(autd3-sample)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(${CMAKE_VERSION} VERSION_GREATER_EQUAL "3.24.0") 
  cmake_policy(SET CMP0135 NEW)
endif()

include(FetchContent)
if(WIN32)
  if(${CMAKE_SYSTEM_PROCESSOR} MATCHES "AMD64")
    FetchContent_Declare(
      autd3
      URL https://github.com/shinolab/autd3-cpp/releases/download/v26.0.0/autd3-v26.0.0-win-x64.zip
    )
  elseif(${CMAKE_SYSTEM_PROCESSOR} MATCHES "ARM64")
    FetchContent_Declare(
      autd3
      URL https://github.com/shinolab/autd3-cpp/releases/download/v26.0.0/autd3-v26.0.0-win-arm.zip
    )
  else()
      message(FATAL_ERROR "Unsupported platform: ${CMAKE_SYSTEM_PROCESSOR}")
  endif()
elseif(APPLE)
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/v26.0.0/autd3-v26.0.0-macos-aarch64.tar.gz
  )
else()
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/v26.0.0/autd3-v26.0.0-linux-x64.tar.gz
  )
endif()
set(USE_SYSTEM_EIGEN OFF)
FetchContent_MakeAvailable(autd3)

add_executable(main main.cpp)

target_link_libraries(main PRIVATE autd3::autd3 autd3::link::soem)

if (CMAKE_GENERATOR MATCHES "Visual Studio")
    set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT main)
endif()
