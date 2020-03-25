import pytesseract
import re
from adhar import get_adhar_front
from preprocessing import text_preprocessing, gray_scaling, noise_removal, scaling


#obtaining text from preprocessed image
def image_preprocess_ocr(image):
    gray_img = gray_scaling.gray_scale(image)
    no_noise_img = noise_removal.image_noise_removal(gray_img)
    text = pytesseract.image_to_string(no_noise_img, config="-l eng+hin")
    text = text_preprocessing.formatting_text(text)
    return text


#obtaining text from raw image
def raw_ocr(image):
    text = pytesseract.image_to_string(image, config="-l eng+tam")
    text = text_preprocessing.formatting_text(text)
    return text