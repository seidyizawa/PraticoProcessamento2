import cv2
import numpy as np
import copy
import array
from matplotlib import pyplot as plt

def limiarizacao(img1):
    #img1 = cv2.GaussianBlur(img1,(5,5),0)
    img3 = cv2.cvtColor(img1,cv2.COLOR_BGR2BGRA)
    img4 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    for i in range(0, img1.shape[0]-1):
        for j in range(0, img1.shape[1]-1):
            if img4.item(i,j,0) >= 0 and img4.item(i,j,0) <= 50 and img4.item(i,j,1) >= 23 and img4.item(i,j,1) <= 68 and img3.item(i,j,2) > 95 and img3.item(i,j,1) > 40 and img3.item(i,j,0) > 20 and img3.item(i,j,2) > img3.item(i,j,1) and img3.item(i,j,2) > img3.item(i,j,0) and abs(img3.item(i,j,2) - img3.item(i,j,1)) > 15 and img3.item(i,j,3) > 15:
            #maxi = max(img1.item(i,j,0),img1.item(i,j,1),img1.item(i,j,2))
            #mini = min(img1.item(i,j,0),img1.item(i,j,1),img1.item(i,j,2))
            #if img1.item(i,j,2) > 95 and img1.item(i,j,1) > 40 and img1.item(i,j,0) > 20 and (maxi - mini) < 15 and abs(img3.item(i,j,2) - img3.item(i,j,1)) > 15 and img1.item(i,j,2) > img1.item(i,j,1) and img1.item(i,j,2) > img1.item(i,j,0):
            #if img1.item(i,j,2) > 220 and img1.item(i,j,1) > 40 and img1.item(i,j,0) > 170 and abs(img3.item(i,j,2) - img3.item(i,j,1)) <= 15 and img1.item(i,j,2) > img1.item(i,j,1) and img1.item(i,j,0) < img1.item(i,j,1):
                img2[i,j] = 255
            else:
                img2[i,j] = 0

    cv2.imwrite('ativ1.png',img2) 
    return img2;

kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
cap.set(3,350)
cap.set(4,240)

while(True):
    ret, imgo = cap.read()
    thr = limiarizacao(imgo)
    cv2.imshow('original',imgo)
    cv2.imshow('threshold',thr)
    cv2.imshow('threshold1',thr2)
    cv2.imshow('threshold2',thr1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break