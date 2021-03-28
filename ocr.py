# Code for OCR
import cv2 
import pytesseract
img = cv2.imread('image4.jpeg')
custom_config = r'--oem 3 --psm 6'
# change tesseract_cmd path if tesseract is installed in a different location. 
# But default location should be this only.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
a = pytesseract.image_to_string(img, config=custom_config)
print(a)








# can run any block of code separately by selecting that part and pressing 
# ctrl + enter
# i have inserted extra space between two blocks of code to show that these 
# codes are not interdependent -you can run them separately 
#(can see the result in the console)

# Code for changing images

import cv2
import numpy as np

#enter your image here
img = cv2.imread('image4.jpeg')
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(np.float32(image), cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 


#PART OF PREPROCESSING- CHANGING IMAGE SIZE
from PIL import Image
#open any image
im = Image.open("image3.jpeg")
im.save("test-600.png", dpi=(300,300)) # OUTPUT TO BE SENT IN BELOW CELL
# print(im.info['dpi'])

im = get_grayscale(im)
#im.show()
# print(im.show())

def rgb2gray(image):
    return cv2.cvtColor(np.float32(image), cv2.COLOR_RGB2GRAY)

img = rgb2gray(Image.open("image4.jpeg"));
#img.show()











# Code for removing shadows


#REMOVING SHADOWS
#INSERT IMAGE OUTPUT THAT WAS PREPROCESSED IN PREVIOUS CELL TO LINE 6
import cv2
img = cv2.imread('image4.jpeg', -1)

rgb_planes = cv2.split(img)

result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

result = cv2.merge(result_planes)
result_norm = cv2.merge(result_norm_planes)

cv2.imwrite('shadows_out.png', result)
cv2.imwrite('shadows_out_norm.png', result_norm)




