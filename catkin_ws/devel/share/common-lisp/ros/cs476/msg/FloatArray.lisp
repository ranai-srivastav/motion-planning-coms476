; Auto-generated. Do not edit!


(cl:in-package cs476-msg)


;//! \htmlinclude FloatArray.msg.html

(cl:defclass <FloatArray> (roslisp-msg-protocol:ros-message)
  ((nums
    :reader nums
    :initarg :nums
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass FloatArray (<FloatArray>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FloatArray>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FloatArray)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs476-msg:<FloatArray> is deprecated: use cs476-msg:FloatArray instead.")))

(cl:ensure-generic-function 'nums-val :lambda-list '(m))
(cl:defmethod nums-val ((m <FloatArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs476-msg:nums-val is deprecated.  Use cs476-msg:nums instead.")
  (nums m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FloatArray>) ostream)
  "Serializes a message object of type '<FloatArray>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'nums))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'nums))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FloatArray>) istream)
  "Deserializes a message object of type '<FloatArray>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'nums) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'nums)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FloatArray>)))
  "Returns string type for a message object of type '<FloatArray>"
  "cs476/FloatArray")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FloatArray)))
  "Returns string type for a message object of type 'FloatArray"
  "cs476/FloatArray")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FloatArray>)))
  "Returns md5sum for a message object of type '<FloatArray>"
  "8a327f765b70d8bd267a8d96beb763ec")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FloatArray)))
  "Returns md5sum for a message object of type 'FloatArray"
  "8a327f765b70d8bd267a8d96beb763ec")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FloatArray>)))
  "Returns full string definition for message of type '<FloatArray>"
  (cl:format cl:nil "float32[] nums~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FloatArray)))
  "Returns full string definition for message of type 'FloatArray"
  (cl:format cl:nil "float32[] nums~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FloatArray>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'nums) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FloatArray>))
  "Converts a ROS message object to a list"
  (cl:list 'FloatArray
    (cl:cons ':nums (nums msg))
))
