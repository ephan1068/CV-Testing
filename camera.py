# Python code to read image
import cv2
import numpy as np 

# To read image from disk, we use
# cv2.imread function, in below method,
frame= cv2.imread("photos/arena_marker.jpg", cv2.IMREAD_COLOR) #read in rame
#loading in the aruco dictionary
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_1000)
arucoParams = cv2.aruco.DetectorParameters_create()
cv2.aruco.draw

#detects the markers
(corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict,
	parameters=arucoParams)

#id contains an array with the ids of detected aruco markers
ids = ids.flatten()

# print(corners)      
# print (ids)

radius = 20
color = (255, 0, 0)
thickness = 2

# Display the resulting frame
# print(ids)
# print(rejected)
for (marker_corner, marker_id) in zip(corners, ids):
    corners = marker_corner.reshape((4, 2))
    # print(corners)
    (c1, c2, c3, c4) = corners

    c1 = [int(c1[0]), int(c1[1])]
    c2 = [int(c2[0]), int(c2[1])]
    c3 = [int(c3[0]), int(c3[1])]
    c4 = [int(c4[0]), int(c4[1])]

    arr = np.array([c1,c2,c3,c4])
    sortedArr = arr[arr[:,0].argsort()]
    print('Sorted 2D Numpy Array')
    arr= np.array([sortedArr[0],sortedArr[1]])
    sortedArr = arr[arr[:,1].argsort()]
    arr= sortedArr[1]

    print(sortedArr)

    frame = cv2.circle(frame, (arr[0],arr[1]), radius, color, thickness)  

cv2.imshow('frame',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
