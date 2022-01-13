import cv2 as cv
import numpy as np

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\berga\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class GoruntuIsleme:

    def goruntuOku(self):
        camera = cv.VideoCapture(0, cv.CAP_DSHOW)
        #kernel = np.ones((1,1), np.uint8)
        while True:
            ret, frame = camera.read()
            #frame = cv.threshold(frame, 128, 255, cv.THRESH_BINARY)
            #frame = cv.erode(frame, kernel, iterations=1)
            #frame = cv.dilate(frame, kernel, iterations=1)
            metin = pytesseract.image_to_string(Image.fromarray(frame), lang='tur')
            print(metin)
            cv.imshow('grunt', frame)
            key = cv.waitKey(1)
            if len(metin) > 3:
                break

        camera.release()
        cv.destroyAllWindows()
        return metin
