;; Auto-generated. Do not edit!


(when (boundp 'cs476::Chain2D)
  (if (not (find-package "CS476"))
    (make-package "CS476"))
  (shadow 'Chain2D (find-package "CS476")))
(unless (find-package "CS476::CHAIN2D")
  (make-package "CS476::CHAIN2D"))

(in-package "ROS")
;;//! \htmlinclude Chain2D.msg.html


(defclass cs476::Chain2D
  :super ros::object
  :slots (_config _W _L _D ))

(defmethod cs476::Chain2D
  (:init
   (&key
    ((:config __config) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:W __W) 0.0)
    ((:L __L) 0.0)
    ((:D __D) 0.0)
    )
   (send-super :init)
   (setq _config __config)
   (setq _W (float __W))
   (setq _L (float __L))
   (setq _D (float __D))
   self)
  (:config
   (&optional __config)
   (if __config (setq _config __config)) _config)
  (:W
   (&optional __W)
   (if __W (setq _W __W)) _W)
  (:L
   (&optional __L)
   (if __L (setq _L __L)) _L)
  (:D
   (&optional __D)
   (if __D (setq _D __D)) _D)
  (:serialization-length
   ()
   (+
    ;; float32[] _config
    (* 4    (length _config)) 4
    ;; float32 _W
    4
    ;; float32 _L
    4
    ;; float32 _D
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _config
     (write-long (length _config) s)
     (dotimes (i (length _config))
       (sys::poke (elt _config i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32 _W
       (sys::poke _W (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _L
       (sys::poke _L (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _D
       (sys::poke _D (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _config
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _config (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _config i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32 _W
     (setq _W (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _L
     (setq _L (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _D
     (setq _D (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get cs476::Chain2D :md5sum-) "d7a949109af612580b026ed4500df1c3")
(setf (get cs476::Chain2D :datatype-) "cs476/Chain2D")
(setf (get cs476::Chain2D :definition-)
      "float32[] config
float32 W
float32 L
float32 D  
")



(provide :cs476/Chain2D "d7a949109af612580b026ed4500df1c3")


