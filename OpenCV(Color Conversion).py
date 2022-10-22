import cv2
import numpy as np

img=cv2.imread("D:\Python\child_loki.jpeg")
img=cv2.resize(img,(450,600))
cv2.imshow("Orginal",img)

# BGR to GRAY Conversion

Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",Gray)

#BGR to HSV Conversion

HSV =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",HSV)
""" Color Conversion
    Comments:
        Cv2.cvtcolor('img',cv2_BGR2GRAY)
        Cv2.cvtcolor('img',cv2_BGR2HSV)
         Color Ratio:
             RED-(255,0,0):Blue-(0,255,0):Green-(0,0,225)
             RBG(0,0,0)-Black
             BBG(128,128,128)-Gray
             RBG(225,225.225)-white"""

