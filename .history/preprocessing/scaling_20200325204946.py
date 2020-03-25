from PIL import Image
import cv2


tempfile ='out.jpg'

#used to set image dpi to 300, increases image quality
def set_image_dpi(image):
    im = Image.open(image)
    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save(tempfile, dpi=(300, 300))
    image = cv2.imread(tempfile)
    return image

