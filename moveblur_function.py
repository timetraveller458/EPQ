import numpy as np
import cv2

def main(img, user_input):
    #shows original image
    cv2.imshow("original", img)
    info = cv2.imread("moving_blur_info.png")
    #shows information image
    cv2.imshow("info", info)
    blurmove = img.copy()
    #splits channels into a blue, green and red array
    channels = cv2.split(img)
    
    #stores width and height of image
    height, width = img.shape[0], img.shape[1]
    #sets kernel size
    k = user_input*2 + 1
    #sets limit to ensure kernel doesn't go beyond the image pixels
    limit = int((k-1)/2)
    #creates empty kernel
    kernel = np.zeros((k,k))
    #sets the middle row of the kernel to 1
    kernel[limit] = 1
    #loops through each channel
    for b in range(3):
        channel = channels[b]
        #loops through each colour for each pixel
        for i in range(limit, height-limit):
          for j in range(limit, width-limit):
            #creates a slice of the image to calculate the average 
            sample = np.zeros((k,k))
            sample = channel[i-limit:i+limit+1,j-limit:j+limit+1]
            sample_move = np.multiply(sample, kernel)
            #calculates mean
            mean_move = np.mean(sample_move)*k
            blurmove[i][j][b] = mean_move
    
    #shows new image
    cv2.imshow("move blur", blurmove)
    #closes all windows when a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()


