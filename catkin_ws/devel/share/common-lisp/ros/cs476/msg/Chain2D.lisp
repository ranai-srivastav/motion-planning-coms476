; Auto-generated. Do not edit!


(cl:in-package cs476-msg)


;//! \htmlinclude Chain2D.msg.html

(cl:defclass <Chain2D> (roslisp-msg-protocol:ros-message)
  ((config
    :reader config
    :initarg :config
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (W
    :reader W
    :initarg :W
    :type cl:float
    :initform 0.0)
   (L
    :reader L
    :initarg :L
    :type cl:float
    :initform 0.0)
   (D
    :reader D
    :initarg :D
    :type cl:float
    :initform 0.0))
)

(cl:defclass Chain2D (<Chain2D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Chain2D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Chain2D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs476-msg:<Chain2D> is deprecated: use cs476-msg:Chain2D instead.")))

(cl:ensure-generic-function 'config-val :lambda-list '(m))
(cl:defmethod config-val ((m <Chain2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs476-msg:config-val is deprecated.  Use cs476-msg:config instead.")
  (config m))

(cl:ensure-generic-function 'W-val :lambda-list '(m))
(cl:defmethod W-val ((m <Chain2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs476-msg:W-val is deprecated.  Use cs476-msg:W instead.")
  (W m))

(cl:ensure-generic-function 'L-val :lambda-list '(m))
(cl:defmethod L-val ((m <Chain2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs476-msg:L-val is deprecated.  Use cs476-msg:L instead.")
  (L m))

(cl:ensure-generic-function 'D-val :lambda-list '(m))
(cl:defmethod D-val ((m <Chain2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs476-msg:D-val is deprecated.  Use cs476-msg:D instead.")
  (D m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Chain2D>) ostream)
  "Serializes a message object of type '<Chain2D>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'config))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'config))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'W))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'L))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'D))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Chain2D>) istream)
  "Deserializes a message object of type '<Chain2D>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'config) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'config)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'W) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'L) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'D) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Chain2D>)))
  "Returns string type for a message object of type '<Chain2D>"
  "cs476/Chain2D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Chain2D)))
  "Returns string type for a message object of type 'Chain2D"
  "cs476/Chain2D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Chain2D>)))
  "Returns md5sum for a message object of type '<Chain2D>"
  "d7a949109af612580b026ed4500df1c3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Chain2D)))
  "Returns md5sum for a message object of type 'Chain2D"
  "d7a949109af612580b026ed4500df1c3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Chain2D>)))
  "Returns full string definition for message of type '<Chain2D>"
  (cl:format cl:nil "float32[] config~%float32 W~%float32 L~%float32 D  ~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Chain2D)))
  "Returns full string definition for message of type 'Chain2D"
  (cl:format cl:nil "float32[] config~%float32 W~%float32 L~%float32 D  ~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Chain2D>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'config) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Chain2D>))
  "Converts a ROS message object to a list"
  (cl:list 'Chain2D
    (cl:cons ':config (config msg))
    (cl:cons ':W (W msg))
    (cl:cons ':L (L msg))
    (cl:cons ':D (D msg))
))
