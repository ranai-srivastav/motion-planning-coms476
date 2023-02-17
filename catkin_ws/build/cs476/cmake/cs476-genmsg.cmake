# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "cs476: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ics476:/root/motion-planning-coms476/catkin_ws/src/cs476/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(cs476_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg" NAME_WE)
add_custom_target(_cs476_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cs476" "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(cs476
  "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs476
)

### Generating Services

### Generating Module File
_generate_module_cpp(cs476
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs476
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(cs476_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(cs476_generate_messages cs476_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg" NAME_WE)
add_dependencies(cs476_generate_messages_cpp _cs476_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cs476_gencpp)
add_dependencies(cs476_gencpp cs476_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cs476_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(cs476
  "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cs476
)

### Generating Services

### Generating Module File
_generate_module_eus(cs476
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cs476
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(cs476_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(cs476_generate_messages cs476_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg" NAME_WE)
add_dependencies(cs476_generate_messages_eus _cs476_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cs476_geneus)
add_dependencies(cs476_geneus cs476_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cs476_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(cs476
  "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs476
)

### Generating Services

### Generating Module File
_generate_module_lisp(cs476
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs476
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(cs476_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(cs476_generate_messages cs476_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg" NAME_WE)
add_dependencies(cs476_generate_messages_lisp _cs476_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cs476_genlisp)
add_dependencies(cs476_genlisp cs476_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cs476_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(cs476
  "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cs476
)

### Generating Services

### Generating Module File
_generate_module_nodejs(cs476
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cs476
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(cs476_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(cs476_generate_messages cs476_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg" NAME_WE)
add_dependencies(cs476_generate_messages_nodejs _cs476_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cs476_gennodejs)
add_dependencies(cs476_gennodejs cs476_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cs476_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(cs476
  "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs476
)

### Generating Services

### Generating Module File
_generate_module_py(cs476
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs476
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(cs476_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(cs476_generate_messages cs476_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/cs476/msg/FloatArray.msg" NAME_WE)
add_dependencies(cs476_generate_messages_py _cs476_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cs476_genpy)
add_dependencies(cs476_genpy cs476_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cs476_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs476)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs476
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(cs476_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cs476)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/cs476
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(cs476_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs476)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs476
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(cs476_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cs476)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/cs476
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(cs476_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs476)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs476\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs476
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(cs476_generate_messages_py std_msgs_generate_messages_py)
endif()
