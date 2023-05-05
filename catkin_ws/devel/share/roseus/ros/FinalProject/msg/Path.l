;; Auto-generated. Do not edit!


(when (boundp 'FinalProject::Path)
  (if (not (find-package "FINALPROJECT"))
    (make-package "FINALPROJECT"))
  (shadow 'Path (find-package "FINALPROJECT")))
(unless (find-package "FINALPROJECT::PATH")
  (make-package "FINALPROJECT::PATH"))

(in-package "ROS")
;;//! \htmlinclude Path.msg.html


(defclass FinalProject::Path
  :super ros::object
  :slots (_path ))

(defmethod FinalProject::Path
  (:init
   (&key
    ((:path __path) ())
    )
   (send-super :init)
   (setq _path __path)
   self)
  (:path
   (&rest __path)
   (if (keywordp (car __path))
       (send* _path __path)
     (progn
       (if __path (setq _path (car __path)))
       _path)))
  (:serialization-length
   ()
   (+
    ;; FinalProject/Point[] _path
    (apply #'+ (send-all _path :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; FinalProject/Point[] _path
     (write-long (length _path) s)
     (dolist (elem _path)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; FinalProject/Point[] _path
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _path (let (r) (dotimes (i n) (push (instance FinalProject::Point :init) r)) r))
     (dolist (elem- _path)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get FinalProject::Path :md5sum-) "b880b1651666aa52142c963a6ef3debf")
(setf (get FinalProject::Path :datatype-) "FinalProject/Path")
(setf (get FinalProject::Path :definition-)
      "Point[] path
================================================================================
MSG: FinalProject/Point
float32 x
float32 y
float32 theta
")



(provide :FinalProject/Path "b880b1651666aa52142c963a6ef3debf")


