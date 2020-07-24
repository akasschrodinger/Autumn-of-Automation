import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

initialFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.flip(frame,1)

    cv2.imshow('frame', frame)
    if cv2.waitKey(0):
        break

    
    initialFrame += 1


laplacian = cv2.Laplacian(frame,cv2.CV_64F)
sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(frame,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()