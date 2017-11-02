cmake_minimum_required(VERSION 2.8)

add_custom_target(
  out-dir ALL
  COMMAND mkdir -p ${CMAKE_SOURCE_DIR}/out
  COMMAND mkdir -p ${CMAKE_SOURCE_DIR}/out/api
  COMMAND mkdir -p ${CMAKE_SOURCE_DIR}/out/libs
  COMMENT "Make out directory"
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  )

add_subdirectory(message)
add_subdirectory(communication)
