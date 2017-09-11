import numpy as np
import cv2
from time import sleep
from scipy import signal

cap = cv2.VideoCapture('output6.avi-Mag20Ideal-lo72-hi92.avi')

frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
outimg = []

window_width = 50
window_height = 30
stride_w = 40
stride_h = 20
frame_shape = (480,640)
projects = np.zeros(shape=(window_width,frames,(1+(frame_shape[1]-window_width)/stride_w)*(1+(frame_shape[0]-window_height)/stride_h))).astype(int)

frame_n = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        patches = 0
        for w in range(0,frame.shape[1]-window_width,stride_w):
            for h in range(0,frame.shape[0]-window_height,stride_h):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                crop = gray[h:h+window_height, w:w+window_width]
                #projects[:,] = np.sum(crop,axis=0)/window_height
                projects[:,frame_n,patches] = ((np.sum(crop,axis=0)/window_height).astype(int))
                #outimg.append(project.astype(int))
                patches+=1
        frame_n+=1
    else:
        break
np.save('project66_all.npy',projects)


# Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()