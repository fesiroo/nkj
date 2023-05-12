import cv2
def photo():
    image = cv2.imread("bangchan.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("bangchan", image)
    cv2.waitKey(0)
photo()
def photo2():
    image = cv2.imread("bangchan.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("bangchan", image)
    cv2.waitKey(0)
photo2()
def rgb():
    image = cv2.imread("bangchan.jpg")
    r, g, b = cv2.split(image)
    cv2.imshow("red", r)
    cv2.imshow("green", g)
    cv2.imshow("blue", b)
    cv2.waitKey(0)
rgb()
def blur():
    image = cv2.imread("bangchan.jpg", cv2.IMREAD_COLOR)
    image_blur = cv2.blur(image, (5,7))
    cv2.imshow("bangchan",image_blur)
    cv2.waitKey(0)
blur()
def cut():
    image = cv2.imread("bangchan.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("bangchan", image [300:700,200:500])
    cv2.waitKey(0)
cut()
