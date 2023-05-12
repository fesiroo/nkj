import cv2 as cv
import numpy as np
image = cv.imread("bangchan.jpg")
# cv.imshow("image", image)
blank = np.zeros(image.shape[:2], dtype="uint8")
# cv.imshow("blank", blank)
mask = cv.circle(blank, (image.shape[1]//2, image.shape[0]//2), 100, 255, -1)
# cv.imshow("circle", mask)
# mask = cv.rectangle(blank,(image.shape[1]//2, image.shape[0]//2),(image.shape[1]//2 +100, image.shape[0]//2 +100), 255, -1)
circle = cv.circle(blank.copy(), (image.shape[1]//2, image.shape[0]//2), 100, 255, -1)
rect = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)
# masked1 = cv.bitwise_and(circle, rect )
masked = cv.bitwise_and(image, image, mask=mask)
cv.imshow("masked", masked)



cv.waitKey(0)


