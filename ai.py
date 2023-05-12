import cv2
def photo():
    image = cv2.imread("yeoo.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("yeosang", image)
    cv2.waitKey(0)
photo()
def photo2():
    image = cv2.imread("yeoo.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("yeosang.png", image)
    cv2.imshow("yeosang", image)
    cv2.waitKey(0)
photo2()
def rgb():
    image = cv2.imread("yeoo.jpg")
    r, g, b = cv2.split(image)
    cv2.imshow("red", r)
    cv2.imshow("green", g)
    cv2.imshow("blue", b)
    cv2.imwrite("ye.png", r)
    cv2.imwrite("y.png", g)
    cv2.imwrite("e.png", b)
    cv2.waitKey(0)
rgb()
def blur():
    image = cv2.imread("yeoo.jpg", cv2.IMREAD_COLOR)
    image_blur = cv2.blur(image, (10,10))
    cv2.imwrite("yeo.blur.png", image_blur)
    cv2.imshow("yeosang",image_blur)
    cv2.waitKey(0)
blur()
def cut():
    image = cv2.imread("yeoo.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("yeosang", image [10:450,300:500])
    cv2.waitKey(0)
cut()

