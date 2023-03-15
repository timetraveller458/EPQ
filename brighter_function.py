import cv2

def main(img, user_input):
    #shows original image
    cv2.imshow("original", img)
    #shows information image
    info = cv2.imread("brightness_info.png")
    cv2.imshow("brightness_info.png", info)
    
    #converts image from BGR to HSV *note that OpenCv uses BGR not RGB* 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #splits channels into h, s and v
    h, s, v = cv2.split(hsv)
    
    #sets the constant to add to existing brightness values
    intensity = user_input*10
    #sets the limit to ensure that brightnesses going above the limit stay at max
    lim = 255 - intensity
    #adds the constant to the original brightness values 
    v[v > lim] = 255
    v[v <= lim] += intensity
    
    #merges the channels back together
    hsv_new = cv2.merge((h,s,v))
    #converts image from HSV to BGR
    img_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)
    
    #shows new image
    cv2.imshow("brighter",img_new)
    #ensure windows are closed when a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()