import cv2

#this function will help in converting RGB image to gray scale
def gray_scale(image):
    #opencv_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    opencv_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite("gray.jpg", opencv_image)
    return opencv_image

#--