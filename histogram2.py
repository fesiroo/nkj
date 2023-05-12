import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("gyu.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
grayhist= cv.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.title("gray")
plt.xlabel("x")
plt.ylabel("#pxl")
plt.plot(grayhist)
plt.xlim(0, 256)
plt.show()