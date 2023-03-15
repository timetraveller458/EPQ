import numpy as np
import cv2

def main(img, user_input):
    #shows original image
    cv2.imshow("original", img)
    
    #shows information image
    info = cv2.imread("blur_info.png")
    cv2.imshow("info", info)
    
    #makes a copy of original image
    blur = img.copy()
    #splits the image into three 2D arrays--blue, green, red values
    channels = cv2.split(img)
    #stores the image height and width
    height, width = img.shape[0], img.shape[1]
    #sets the kernel size
    k = user_input*2 + 1

    #sets a limit so the kernel doesn't go beyond the pixels and cause an error
    limit = int((k-1)/2)
    
    #loops through each channel
    for k in range(3):
        channel = channels[k]
        #loops through each colour value for a pixel
        for i in range(limit, height-limit):
          for j in range(limit, width-limit):
            #creates a slice of the image to calculate the average
            sample = np.zeros((k,k))
            sample = channel[i-limit:i+limit+1,j-limit:j+limit+1]          
            
            #calculates mean and sets new pixel value in the new image
            mean = np.mean(sample)
            blur[i][j][k] = mean
    
    
    #shows new image
    cv2.imshow("blur", blur)
    #ensures all windows close when a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
