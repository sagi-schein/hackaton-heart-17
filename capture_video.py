import numpy as np
import cv2

cap = cv2.VideoCapture(0)
x = 100
y = 100
r = 30

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.circle(gray,(x,y),r,(0,0,255))
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1)& 0xFF == ord('z'):
        x -=5
    if cv2.waitKey(1) & 0xFF == ord('c'):
        x+=5
    if cv2.waitKey(1) & 0xFF == ord('s'):
        y-=5
    if cv2.waitKey(1) & 0xFF == ord('x'):
        y+=5
    if cv2.waitKey(1) & 0xFF == ord('e'):
        r+=5
    if cv2.waitKey(1) & 0xFF == ord('w'):
        r-=5
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


'''
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
'''