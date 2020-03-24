import sys
#sys.path.append('Users/sahana/Desktop/ocr_for_actyv(4/03)')
import cv2
from preprocessing import gray_scaling, scaling, noise_removal,text_preprocessing
from adhar import get_adhar_front, get_adhar_back
from ocr import ocr
import config as cfg



#CHECKING IF THE IMAGE IS ADHAR BACK OR NOT
def is_adhar_back(processed_img_text, raw_image_text):
    return get_adhar_back.check_adhar_back(processed_img_text, raw_image_text)


#CHECKING IF THE IMAGE IS ADHAR FRONT OR NOT
def is_adhar_front(processed_img_text, raw_image_text):
    return get_adhar_front.check_adhar_front(processed_img_text, raw_image_text)




#CHECKING THE TYPE OF DOC AND GETTING FIELDS
def steps(image_file):    

    #Getting text from ocr (preprocessed image text & raw image text)
    processed_img_text = ocr.preprocessed_ocr(image_file)
    raw_image_text = ocr.raw_ocr(image_file)

    #CHECKING AND GETTINGS FIELDS FROM ADHAR BACK
    if is_adhar_back(processed_img_text, raw_image_text):
        adhar_back_text = get_adhar_back.get_details_adhar_back(raw_image_text)
        return adhar_back_text


    #CHECKING AND GETTINGS FIELDS FROM ADHAR FRONT
    if is_adhar_front(processed_img_text, raw_image_text):
        adhar_front_text = get_adhar_front.get_details_adhar_front(processed_img_text, raw_image_text)
        return adhar_front_text


    return cfg.ERROR_MESSAGE

    

# import pdb; pdb.set_trace()
# import os
# image_file.seek(0, os.SEEK_END)
# size = image_file.tell()
# print(size)