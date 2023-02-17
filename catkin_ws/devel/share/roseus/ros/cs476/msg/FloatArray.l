;; Auto-generated. Do not edit!


(when (boundp 'cs476::FloatArray)
  (if (not (find-package "CS476"))
    (make-package "CS476"))
  (shadow 'FloatArray (find-package "CS476")))
(unless (find-package "CS476::FLOATARRAY")
  (make-package "CS476::FLOATARRAY"))

(in-package "ROS")
;;//! \htmlinclude FloatArray.msg.html


(defclass cs476::FloatArray
  :super ros::object
  :slots (_nums ))

(defmethod cs476::FloatArray
  (:init
   (&key
    ((:nums __nums) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _nums __nums)
   self)
  (:nums
   (&optional __nums)
   (if __nums (setq _nums __nums)) _nums)
  (:serialization-length
   ()
   (+
    ;; float32[] _nums
    (* 4    (length _nums)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _nums
     (write-long (length _nums) s)
     (dotimes (i (length _nums))
       (sys::poke (elt _nums i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _nums
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _nums (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _nums i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get cs476::FloatArray :md5sum-) "8a327f765b70d8bd267a8d96beb763ec")
(setf (get cs476::FloatArray :datatype-) "cs476/FloatArray")
(setf (get cs476::FloatArray :definition-)
      "float32[] nums
")



(provide :cs476/FloatArray "8a327f765b70d8bd267a8d96beb763ec")


