import cv2
import numpy as np
import glob

CHECKERBOARD = (4,7) # 행, 열(체커보드 내부 코너 수)

# criteria: 반복을 종료할 조건 (type(종료 조건의 타입), max_iter(최대 반복할 횟수), epsilon(정확도))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objpoints = [] 
imgpoints = [] 

objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None

images = glob.glob('./img/*.jpg')

for fname in images:
    img = cv2.imread(fname)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # ret(true or false), corners(감지된 코너) = cv2.findChessboardCorners(image, pattern_size, flags(작업 플래그))
    ret, corners = cv2.findChessboardCorners(gray,
                                             CHECKERBOARD,
                                             cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    if ret == True:
        objpoints.append(objp)

        # 정확한 코너의 위치를 얻기위함
        # cv2.cornerSubPix(image, corners, win_size, zero_zone, criteria)
        # win_size(검색 창의 측면 길이의 절반(무슨소리인지 모르겠음))
        # zero_zone(사각 영역의 크기의 절반, 보통 (-1,-1)사용함 (사각 영역이 없음을 나타냄))
        corners2 = cv2.cornerSubPix(gray, corners, (11,11),(-1,-1), criteria)
        imgpoints.append(corners2)

        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)

    cv2.imshow('img',img)
    cv2.waitKey(200)

cv2.destroyAllWindows()

# cv2.calibrateCamera(object_points, image_points, image_size)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None) 
# 사용하는 변수: mtx = 내부 카메라 행결, dist = 렌즈 왜곡 계수

print("mtx : \n")
print(mtx)

print("dist : \n")
print(dist)

print("rvecs : \n")
print(rvecs)

print("tvecs : \n")
print(tvecs)