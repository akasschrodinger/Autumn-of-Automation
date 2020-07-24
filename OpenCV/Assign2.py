import cv2
import numpy as np
from matplotlib import pyplot as plt  

img= cv2.imread('picture.jpg', 0)
rows,cols= img.shape


for i in range(4):
	M=np.float32([[1,0,25*i],[0,1,25*i]])
	dst= cv2.warpAffine(img,M,(cols,rows))

	cv2.imshow('img', dst)
	cv2.waitKey(1000)
	cv2.destroyAllWindows()

for i in range(4):
	M= cv2.getRotationMatrix2D((cols/2*(i+1), rows/2*(i+1)), 10, 1)
	dst = cv2.warpAffine(img,M,(cols,rows))

	cv2.imshow('img', dst)
	cv2.waitKey(1000)
	cv2.destroyAllWindows()

blur = cv2.blur(img, (5,5))
blur2=cv2.blur(img, (10,10))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.show()
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur2), plt.title('Blurred2')
plt.xticks([]), plt.yticks([])
plt.show()




