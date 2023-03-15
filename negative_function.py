import cv2

def main(img): 
    #shows original image
    cv2.imshow("original", img)
    #shows information image
    info = cv2.imread("negative_info.png")
    cv2.imshow("info", info)
    #calculates negative
    new = 255 - img
    
    #shows new image
    cv2.imshow("negative", new)
    #closes all windows when a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()