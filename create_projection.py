import numpy as np
import cv2
from time import sleep
from scipy import signal

#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('output5.avi')
cap = cv2.VideoCapture('output6.avi-Mag20Ideal-lo72-hi92.avi')

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('project5.avi',fourcc, 20.0, (30,400))
outimg = []

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #crop = gray[160:190,280:330]
        crop = gray[200:230, 290:340]
        project = np.sum(crop,axis=0)/30
        outimg.append(project.astype(int))
        # write the flipped frame
        #out.write(gray)
        sleep(0.05)
        cv2.imshow('frame',crop)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
outimg = np.array(outimg)
cv2.imwrite('project6.jpg',outimg)


# Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()