# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "FinalProject: 2 messages, 0 services")

set(MSG_I_FLAGS "-IFinalProject:/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(FinalProject_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg" NAME_WE)
add_custom_target(_FinalProject_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "FinalProject" "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg" "FinalProject/Point"
)

get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg" NAME_WE)
add_custom_target(_FinalProject_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "FinalProject" "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg"
  "${MSG_I_FLAGS}"
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/FinalProject
)
_generate_msg_cpp(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/FinalProject
)

### Generating Services

### Generating Module File
_generate_module_cpp(FinalProject
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/FinalProject
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(FinalProject_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(FinalProject_generate_messages FinalProject_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_cpp _FinalProject_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_cpp _FinalProject_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(FinalProject_gencpp)
add_dependencies(FinalProject_gencpp FinalProject_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS FinalProject_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg"
  "${MSG_I_FLAGS}"
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/FinalProject
)
_generate_msg_eus(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/FinalProject
)

### Generating Services

### Generating Module File
_generate_module_eus(FinalProject
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/FinalProject
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(FinalProject_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(FinalProject_generate_messages FinalProject_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_eus _FinalProject_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_eus _FinalProject_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(FinalProject_geneus)
add_dependencies(FinalProject_geneus FinalProject_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS FinalProject_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg"
  "${MSG_I_FLAGS}"
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/FinalProject
)
_generate_msg_lisp(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/FinalProject
)

### Generating Services

### Generating Module File
_generate_module_lisp(FinalProject
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/FinalProject
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(FinalProject_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(FinalProject_generate_messages FinalProject_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_lisp _FinalProject_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_lisp _FinalProject_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(FinalProject_genlisp)
add_dependencies(FinalProject_genlisp FinalProject_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS FinalProject_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg"
  "${MSG_I_FLAGS}"
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/FinalProject
)
_generate_msg_nodejs(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/FinalProject
)

### Generating Services

### Generating Module File
_generate_module_nodejs(FinalProject
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/FinalProject
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(FinalProject_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(FinalProject_generate_messages FinalProject_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_nodejs _FinalProject_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_nodejs _FinalProject_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(FinalProject_gennodejs)
add_dependencies(FinalProject_gennodejs FinalProject_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS FinalProject_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg"
  "${MSG_I_FLAGS}"
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/FinalProject
)
_generate_msg_py(FinalProject
  "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/FinalProject
)

### Generating Services

### Generating Module File
_generate_module_py(FinalProject
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/FinalProject
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(FinalProject_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(FinalProject_generate_messages FinalProject_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Path.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_py _FinalProject_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/motion-planning-coms476/catkin_ws/src/FinalProject/msg/Point.msg" NAME_WE)
add_dependencies(FinalProject_generate_messages_py _FinalProject_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(FinalProject_genpy)
add_dependencies(FinalProject_genpy FinalProject_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS FinalProject_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/FinalProject)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/FinalProject
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(FinalProject_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/FinalProject)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/FinalProject
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(FinalProject_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/FinalProject)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/FinalProject
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(FinalProject_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/FinalProject)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/FinalProject
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(FinalProject_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/FinalProject)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/FinalProject\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/FinalProject
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(FinalProject_generate_messages_py std_msgs_generate_messages_py)
endif()
