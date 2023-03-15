import numpy as np
import cv2

def main(img):
    #shows original image
    cv2.imshow("original", img)
    #shows information image
    info = cv2.imread("skew_info.png")
    #resize image
    info = cv2.resize(info, (0,0), fx=0.6,fy=0.6)
    cv2.imshow("info", info)
    
    #final coordinates
    q = [[48],[50],[48],[100],[212],[50]]
    
    #matrix of original coordinates
    m = [[18,47,1,0,0,0],
         [0,0,0,18,47,1],
         [15,100,1,0,0,0],
         [0,0,0,15,100,1],
         [178,6,1,0,0,0],
         [0,0,0,178,6,1]]
    
    #inverse of m
    invm = np.linalg.inv(m)
    #multiplies inverse of m with q
    a = np.matmul(invm,q)
    
    #reformats the coefficients of transformation function
    a_format = np.array([[float(a[0]),float(a[1]),float(a[2])],
                          [float(a[3]),float(a[4]),float(a[5])]])
    
    #applies the transfer function
    warp = cv2.warpAffine(img, a_format, (img.shape[1],img.shape[0]))

    #shows new image
    cv2.imshow("skew", warp)
    #ensures windows close after a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    