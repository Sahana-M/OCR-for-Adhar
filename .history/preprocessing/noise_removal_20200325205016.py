import cv2
import numpy as np


#used to remove the noise from the image
def image_noise_removal(img):
   filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 2)
   kernel = np.ones((1,1), np.uint8)
   dilated = cv2.dilate(filtered,kernel,iterations = 1)
 
   img = cv2.medianBlur(dilated,5)
   or_image = cv2.bitwise_or(img, dilated)
 
   blur = cv2.medianBlur(or_image, 3)
   f_image = cv2.bitwise_or(or_image, blur)
 
   f_image = cv2.fastNlMeansDenoising(f_image,None,10,7,21)
  
   return f_image