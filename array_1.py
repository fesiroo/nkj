import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui
import time
# ar = np.array([1,4,2,3,5])
# ar1 = np.arange(5)
# print(ar)
# print(ar1)
# print(ar + ar1)
# print(ar<5)
# print(ar[ar>3])
# print(ar[0:3])
# print(ar.min())
# print(ar.max())
# print(np.random.permutation(5))
# ar2 = np.arange(10)
# ar3 = np.arange(8)
# print(ar2.reshape(2,5))
# print(ar3.reshape(2,2,2))
# while True:
#     screen = np.array(ImageGrab.grab(bbox=(1182,270, 1378,384)))
#     cv2.imshow("window", screen)
#     a = np.array([[1182,270],[1378,384]])
#     mask1 = mask(screen, a)
#     cv2.imshow("w2", mask1)
#     cv2.waitKey(0)

def mask(screen, a):
    mask1 = np.zeros_like(screen)
    cv2.fillPoly(mask1, a, 255)
    mask2 = cv2.bitwise_and(screen, mask1)
    return mask1
while True:
    screen = np.array(ImageGrab.grab(bbox=(800, 400, 1200, 600)))
    cv2.imshow("window", screen)
    a = np.array([[0,200],[200,0], [400,200]])
    mask3 = mask(screen, a)
    cv2.imshow("w2", mask3)
    cv2.waitKey(0)
    
def position():
    while True:
        print(pyautogui.position())
        time.sleep(5)
# position()
# 804,295, 983,404
# 1177,160,1058,276
# 1182,270, 1378,384