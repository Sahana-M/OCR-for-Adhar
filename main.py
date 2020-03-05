import sys
sys.path.append('Users/sahana/Desktop/ocr_for_actyv(4/03)')
import cv2
from deskewing import deskew
from pyimagesearch.transform import four_point_transform
import matplotlib.pyplot as plt

images = ['a1.jpg', 'a2.jpg', 'a3.jpg', 'a4.jpg', 'a5.jpg',
            'a6.jpg', 'a7.jpg', 'a8.jpg', 'a9.jpg', 'a10.jpg', 'a11.jpg', 'someadhar.jpg']



for image in images:
    image_path = 'images/'+image
    image = cv2.imread(image_path)
    rotated , coords = deskew.deskew(image)
    image = four_point_transform(image, coords)
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax1.imshow(image)
    ax2 = fig.add_subplot(2,2,2)
    ax2.imshow(rotated)
    plt.show()
    cv2.waitKey(0)
