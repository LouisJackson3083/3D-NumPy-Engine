import numpy as np

class Camera():
    def __init__(self, width, height):
        focal_length = 500
        self.intrinsic_matrix = np.array([ 
            [focal_length, 0, width/2], 
            [0, focal_length, height/2], 
            [0, 0, 1] 
        ]) 
        self.rotation = np.array([0, 0, 0], dtype=np.float32)  # rotation vector (pitch,yaw,roll)
        self.translation = np.array([0, 0, 100], dtype=np.float32)  # translation vector (x,y,z)

    def HandleInput(self, input):
        if (input == ord('w')):
            self.translation[0] += 1
        elif (input == ord('s')):
            self.translation[0] -= 1
        elif (input == ord('a')):
            self.translation[2] += 1
        elif (input == ord('d')):
            self.translation[2] -= 1
            
        elif (input == ord('i')):
            self.rotation[0] += 1
        elif (input == ord('k')):
            self.rotation[0] -= 1
        elif (input == ord('j')):
            self.rotation[1] += 1
        elif (input == ord('l')):
            self.rotation[1] -= 1