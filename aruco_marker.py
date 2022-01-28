# Python code to read image
import cv2
import numpy as np 

# To read image from disk, we use
# cv2.imread function, in below method,
frame= cv2.imread("photos/arena.jpg", cv2.IMREAD_COLOR)
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_1000)
arucoParams = cv2.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict,
	parameters=arucoParams)
ids = ids.flatten()
print(corners)      
# Loop over the detected ArUco corners
  
# Display the resulting frame
cv2.imshow('frame',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(corners.flatten())