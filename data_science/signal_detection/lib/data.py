import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
import os

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
folder = "images/N"
counter = 0

if not os.path.exists(folder):
    os.makedirs(folder)

try:
    while True:
        aux, img = cap.read()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            imgWhite = np.ones((300,300,3), np.uint8)*255
            Crop = img[y-20:y+h+20, x-20:x+w+20]

            aspectRatio = h/w
            if aspectRatio > 1:
                aux2 = 300/h
                cal = math.ceil(aux2*w)
                imgResize = cv2.resize(Crop,(cal,300))
                gap = math.ceil((300-cal)/2)
                imgWhite[:, gap:cal+gap] = imgResize
            else:
                aux2 = 300/w
                cal2 = math.ceil(aux2*h)
                imgResize = cv2.resize(Crop,(300,cal2))
                gap2 = math.ceil((300-cal2)/2)
                imgWhite[gap2:cal2+gap2, :] = imgResize

            cv2.imshow('imageCrop',imgWhite)

        cv2.imshow('image',img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            counter += 1
            filename = f'{folder}/imagem_{time.time()}.jpg'
            cv2.imwrite(filename, imgWhite)
            print(counter)

except KeyboardInterrupt:
    cv2.imwrite(f'{folder}/imagem_{time.time()}.jpg', imgWhite)
    cap.release()
    cv2.destroyAllWindows()

