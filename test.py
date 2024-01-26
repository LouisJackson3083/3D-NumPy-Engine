import numpy as np 
import cv2 
from camera import Camera
  
# Define the camera

image_width = 640
image_height = 480
camera = Camera(image_width, image_height)

# Define the 3D point in the world coordinate system 
x, y, z = 0, 0, 0
points_3d = np.array([[[x, y, z]]], np.float32) 

while (True):
    # Project 3D points onto 2D plane 
    points_2d, _ = cv2.projectPoints(
        points_3d, 
        camera.rotation, 
        camera.translation.reshape(-1, 1), 
        camera.intrinsic_matrix, 
        None
    ) 
    
    # Plot 2D points 
    img = np.zeros((image_height, image_width),  
                dtype=np.uint8) 
    for point in points_2d.astype(int): 
        img = cv2.circle(img, tuple(point[0]), 2, 255, -1) 

    cv2.imshow('Image', img)

    
    input = cv2.waitKey(0)
    print(input)
    camera.HandleInput(input)
    if input == ord('q'):
        break
cv2.destroyAllWindows() 