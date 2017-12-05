try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import cv2
import os
from gtts import gTTS

#pytesseract.pytesseract.tesseract_cmd = 'full address of tesseract.exe'
#Include the above line, if you don't have tesseract executable in your PATH
#Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

print(pytesseract.image_to_string(Image.open('2345.jpg')))
#im = Image.open('2534.jpg')
'''
im = cv2.imread("2534.jpg",cv2.IMREAD_COLOR)
gr = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(gr, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite("2534_1.jpg",th)
'''
##cap = cv2.VideoCapture(2)
##cv2.namedWindow('yo')
##cv2.waitKey(0)
##_,img = cap.read()
##cv2.imwrite('2345.jpg',img)
##img = Image.open('2345.jpg')
##text = pytesseract.image_to_string(img)
##print(text)
##tts = gTTS(text, lang='en')
##tts.save("yo1.mp3")
##os.system("yo1.mp3")

