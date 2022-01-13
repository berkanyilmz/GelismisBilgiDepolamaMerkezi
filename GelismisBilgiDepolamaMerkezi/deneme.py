import cv2 as cv
import numpy as np

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\berga\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def metinOku():
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    # kernel = np.ones((1, 1), np.uint8)
    metin = ''
    while True:
        _, frame = cap.read()
        imgH, imgW, _ = frame.shape
        # frame = cv.erode(frame, kernel, iterations=1)
        # frame = cv.dilate(frame, kernel, iterations=1)
        metin = pytesseract.image_to_string(Image.fromarray(frame))
        cv.imshow("Goruntu", frame)
        print(metin)
        if len(metin) > 3:
            break
    print("Kelime : ", metin)
    cap.release()
    cv.destroyAllWindows()

metinOku()