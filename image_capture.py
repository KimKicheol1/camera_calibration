import cv2

camera = cv2.VideoCapture(0)
i = 1

while True:
  _, img = camera.read()
  
  cv2.imshow('img', img)
  
  if cv2.waitKey(1) == ord('c'):
    cv2.imwrite(f'./img/calib_image{i}.jpg',img)
    i += 1
  
  if cv2.waitKey(1) == ord('q'):
    break

cv2.destroyAllWindows()
camera.release()
