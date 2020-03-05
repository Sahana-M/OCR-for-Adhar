import cv2
import numpy as np


angles = [90.0, -90.0, 0.0, -0.0]
def deskew(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    print("test : ",cv2.minAreaRect(coords))



    if angle<-10 and angle>-85:
        print("1st angle before : ", angle)
        angle = -(90+angle)
        print("1st angle after : ", angle)
    elif angle <= -85 and angle > -90:  
        print("2nd place : ", angle)                             #angle is 0 or -0 degree
        angle = -90 - angle
    else:
        angle = -angle



    #print(image)
    (h,w) = image.shape[:2]
    print("(h,w) : ", h,w)
    center = (w//2, h//2)
    print("center : " , center)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    #print("rotated:", rotated)
    cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
	(10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
    # show the output image
    print("[INFO] angle: {:.3f}".format(angle))
    #cv2.imwrite("out.jpg", rotated)
    return rotated, coords









