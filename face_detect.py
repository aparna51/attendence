import cv2
import numpy as np
import os




cam=cv2.VideoCapture(0)

width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
video_frame=cv2.VideoWriter_fourcc(*'XVID')
video_output=cv2.VideoWriter('a.avi',video_frame,50.0,(int(width),int(height)))

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(cam.isOpened):
  x,frame=cam.read()
  faces=face_cascade.detectMultiScale(frame,scaleFactor=1.05,minNeighbors=5)

  for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        img=frame[x:x+w,y:y+h]



  cv2.imshow("cam",frame)

  if cv2.waitKey(1) & 0xFF==ord('q'):
    break



cv2.waitKey(0)
cv2.destroyAllWindows()
cam.release
