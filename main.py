import sys
sys.path.append('Users/sahana/Desktop/ocr_for_actyv(4/03)')
import cv2
from deskewing import deskew
from preprocessing import gray_scaling, scaling, noise_removal
from ocr import ocr
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output


images = ['images/a1.jpg']


for l in range(1):
    image_path = images[l]

    img = cv2.imread(image_path)

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    print(d.keys())

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 10:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = pytesseract.image_to_string(img, config = '-l eng+tam')
            print("\n", text)


    cv2.imwrite('out.jpg', img)


    
    # if(len(text) < 3):
        #SCALING
    scaled_img = scaling.set_image_dpi(image_path)

        #GRAY SCALING SCALING IN 
    gray_img = gray_scaling.gray_scale(scaled_img)
        
        #NOISE REMOVAL
    no_noise_img = noise_removal.image_noise_removal(gray_img)

    # fig = plt.figure()
    # ax1 = fig.add_subplot()
    # ax1.imshow(no_noise_img)
    # plt.show()
    

    text = ocr.ocr(no_noise_img)
    
    print("\n----------------------\ntext : ", text )
    
    # else:
    #print(text)
