import cv2
import sys

img=cv2.imread("image.jpg")

if img is None:
	sys.exit("Could not find the image")

cv2.imshow("Display image", img)
k= cv2.waitKey(0)

gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GREY)

cv2.imwrite("new image.png", gray_img)
cv2.imshow("new image grayscale", gray_img)
cv2.waitKey(0)


