
(cl:in-package :asdf)

(defsystem "cs476-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Chain2D" :depends-on ("_package_Chain2D"))
    (:file "_package_Chain2D" :depends-on ("_package"))
  ))