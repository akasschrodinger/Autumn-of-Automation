import cv2
import numpy as np

# Capturing video from webcam:
cap = cv2.VideoCapture(0)

initialFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.flip(frame,1)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
    initialFrame += 1


cap.release()
cv2.destroyAllWindows()

#to start the webcam, run the code.
#to end, press 'q' .