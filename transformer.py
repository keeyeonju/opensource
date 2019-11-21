import numpy as np
import cv2

file = 'test.mp4'
cap = cv2.VideoCapture(file)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()