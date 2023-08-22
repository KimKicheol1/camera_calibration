import numpy as np
import cv2

def camera_calibration(img):
  ret = 0.4182764049129663
  mtx = np.array([[781.39964175, 0, 635.08153277], [0, 783.69511144, 370.11868048], [0, 0, 1]]) 
  dist = np.array([[-0.35731871, 0.17285701, 0.00074883, -0.00051063, -0.05188869]])
  
  h, w = img.shape[:2]
  newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
  
  dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
  
  x, y, w, h = roi
  dst = dst[y: y+h, x: x+w]
  
  return dst

camera = cv2.VideoCapture("rtsp://administrator:jakazuadmin@192.168.0.117:554/stream1") # ip camera  addr

while True:
  _, img = camera.read()
  
  result = camera_calibration(img)
  
  cv2.imshow('Original Image', img)
  cv2.imshow('Calibration Image', result)
  
  if cv2.waitKey(1) == ord('q'):
    break

cv2.destroyAllWindows()
camera.release()