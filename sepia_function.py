
import numpy as np
import cv2

def main(img):
    #shows original image
    cv2.imshow("original", img)
    #shows information image
    info = cv2.imread("sepia_info.png")
    cv2.imshow("info", info)
    #stores coefficients to calculate the new values
    coeffs =   [[0.189, 0.769, 0.393],[0.168, 0.686, 0.349],[0.131, 0.534, 0.272]]    
    new = []

    #loops through each channel    
    for i in range(3):
        #applies the coefficients to the existing values
        red = img[:,:,2].copy()
        temp = np.zeros(red.shape) + coeffs[i][2]
        red = np.multiply(temp, red)
        
        green = img[:,:,1].copy()
        temp = np.zeros(green.shape) + coeffs[i][1]
        green = np.multiply(temp, green)
        
        blue = img[:,:,0].copy()
        temp = np.zeros(blue.shape) + coeffs[i][0]
        blue = np.multiply(temp, blue)
        
        new.append(red + green + blue)
       
    #changes values over the max to the max
    new[0][new[0] > 255] = 255
    new[1][new[1] > 255] = 255
    new[2][new[2] > 255] = 255
    
    #makes sure they are the right data type
    new[2] = new[2].astype("uint8")
    new[1] = new[1].astype("uint8")
    new[0] = new[0].astype("uint8")
    
    #merges channels together
    sepia = cv2.merge((new[2], new[1], new[0]))
    
    #shows new image
    cv2.imshow("sepia", sepia)
    #close all windows when a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    