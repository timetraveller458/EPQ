import numpy as np
import cv2

def main(img, user_input):
    #shows original image
    cv2.imshow("original", img)
    #shows information image
    info = cv2.imread("chrom_abr_info.png")
    cv2.imshow("info", info)
    #splits channels into blue, green and red arrays
    b,g,r = cv2.split(img)
    
    #sets shift value
    k = user_input*10
    
    #applies shift to the blue channel
    shift = b[:-k]
    add = np.zeros((b[:k].shape))
    newb = b.copy()
    newb[:k] = add
    newb[k:] = shift
    
    #applies half a shift to the red channel
    shift = r[:-int(k/2)]
    add = np.zeros((r[:int(k/2)].shape))
    newr = r.copy()
    newr[:int(k/2)] = add
    newr[int(k/2):] = shift
    
    #merges channels together
    new = cv2.merge((newb,g,newr))
    
    #shows new image
    cv2.imshow("chromatic aberration", new)
    #ensures windows are closed when a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
