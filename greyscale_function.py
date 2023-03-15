import cv2

def main(img): 
    #shows original image
    cv2.imshow("original", img)
    #shows information image
    info = cv2.imread("greyscale_info.png")
    cv2.imshow("info", info)
    #splits channels into blue, green and red arrays
    b,g,r = cv2.split(img)
    
    #takes an average of the three channels
    average = b/3 + g/3 + r/3
    #makes sure the array has the correct data type
    average = average.astype("uint8")    
    
    #merges 3 average arrays as though they are the blue, green and red channels
    new = cv2.merge((average,average,average))
    
    #shows new image
    cv2.imshow("greyscale", new)
    #closes all windows after a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    