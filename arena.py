import math
import processed_marker
import numpy as np
import cv2

width = 4.0
height = 2.0
m_list = []
def getHomographyMatrix(frame,marker_list):
    for x in marker_list:
        if x.id == 0:  #finding all the corners of the arena
            pt00 = x.corner1
        elif x.id == 1:
            pt40 = x.corner1
        elif x.id == 2:
            pt02 = x.corner1
        elif x.id == 3:
            pt42 = x.corner1
        
    src_pts = np.float32([pt00, pt40, pt02, pt42]) #pixel coordinates of the markers
    dst_pts = np.float32([[0.0, 0.0], [width, 0.0], [0.0, height], [width, height]]) #arena coordinates of markers
    H = cv2.getPerspectiveTransform(src_pts, dst_pts)
    #print(H.shape)
    return H


def processMarkers(frame, marker_list, H):
    for x in marker_list:
        if x.id > 3:
            n_marker = translate(x, H)
            #print(x.id)
            m_list.append(n_marker)
            
            #Add a green arrowed line
            frame = cv2.arrowedLine(frame,(int(x.corner1[0]), int(x.corner1[1])),(int(x.corner2[0]), 
            int(x.corner2[1])),(0, 255, 0),2,tipLength= .4)
    frame = createObstacles(frame,H)
    return frame
def createObstacles(frame,H):
    #
    #50cm -y
    #20cm -x
    #.55 is the x-coord of the obj and 
    possible_x = [0.55, 1.5, 2.3]
    possible_y = [0.25,0.75,1.25]
   
    x_length = 0.2
    y_length = 0.5
    point1 = np.float32(np.array([[[possible_x[1], possible_y[1]]]]))
    point2 = np.float32(np.array([[[possible_x[1] + x_length, possible_y[1] + y_length]]]))
    point3 = np.float32(np.array([[[1.6, 0.50]]]))
    inverse_matrix = np.linalg.pinv(H)
    transformed_1 = cv2.perspectiveTransform(point1, inverse_matrix)
    transformed_2 = cv2.perspectiveTransform(point2, inverse_matrix)
    text = cv2.perspectiveTransform(point3, inverse_matrix)
    print(transformed_1)
    print(transformed_2)
    frame = cv2.rectangle(frame,(int(transformed_1[0,0,0]),int(transformed_1[0,0,1])),
        (int(transformed_2[0,0,0]),int(transformed_2[0,0,1])),(185,146,68),3)
    frame = cv2.putText(frame, 'S', (int(text[0,0,0]),int(text[0,0,1])), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
    print("not implemented yet")

    point1 = np.float32(np.array([[[possible_x[2], possible_y[2]]]]))
    point2 = np.float32(np.array([[[possible_x[2] + x_length, possible_y[2] + y_length]]]))
    point3 = np.float32(np.array([[[1.6, 0.50]]]))
    inverse_matrix = np.linalg.pinv(H)
    transformed_1 = cv2.perspectiveTransform(point1, inverse_matrix)
    transformed_2 = cv2.perspectiveTransform(point2, inverse_matrix)
    text = cv2.perspectiveTransform(point3, inverse_matrix)
    print(transformed_1)
    print(transformed_2)
    frame = cv2.rectangle(frame,(int(transformed_1[0,0,0]),int(transformed_1[0,0,1])),
        (int(transformed_2[0,0,0]),int(transformed_2[0,0,1])),(185,146,68),3)


    point1 = np.float32(np.array([[[possible_x[1], possible_y[0]]]]))
    point2 = np.float32(np.array([[[possible_x[1] + x_length, possible_y[0] + y_length]]]))
    point3 = np.float32(np.array([[[1.6, 0.50]]]))
    inverse_matrix = np.linalg.pinv(H)
    transformed_1 = cv2.perspectiveTransform(point1, inverse_matrix)
    transformed_2 = cv2.perspectiveTransform(point2, inverse_matrix)
    text = cv2.perspectiveTransform(point3, inverse_matrix)
    print(transformed_1)
    print(transformed_2)
    frame = cv2.rectangle(frame,(int(transformed_1[0,0,0]),int(transformed_1[0,0,1])),
        (int(transformed_2[0,0,0]),int(transformed_2[0,0,1])),(25,177,215),3)
    return frame     

def translate(marker, H):
    # find the center of the marker in pixels
    marker_coords_px = np.float32(np.array([[[0.0, 0.0]]]))  # dont know why you need so many brakets, but this makes it work
    marker_coords_px[0, 0, 0] = (marker.corner1[0] + marker.corner2[0] + marker.corner3[0] + marker.corner4[0]) / 4
    marker_coords_px[0, 0, 1] = (marker.corner1[1] + marker.corner2[1] + marker.corner3[1] + marker.corner4[1]) / 4

    # Use homography transformation matrix to convert marker coords in px to meters
    marker_coords_m = cv2.perspectiveTransform(marker_coords_px, H)[0]
    #print(marker_coords_m)

    # Find theta of the marker
    corner1_coords_m = cv2.perspectiveTransform(np.float32(np.array([[marker.corner1]])), H)
    corner2_coords_m = cv2.perspectiveTransform(np.float32(np.array([[marker.corner2]])), H)
    marker_theta = math.atan2(corner2_coords_m[0, 0, 1] - corner1_coords_m[0, 0, 1], corner2_coords_m[0, 0, 0] - corner1_coords_m[0, 0, 0])
    #print(marker_theta)
    n_marker = processed_marker.processed_Marker(marker.id, marker_coords_m[0,0], marker_coords_m[0,1], marker_theta)

    return n_marker