import numpy as np
import cv2
from scipy import fft
import matplotlib.pyplot as plt

projects = np.load('project66_all.npy')

#img = cv2.imread('project6.jpg',0)
total_fft = np.zeros(64)
for i in range(projects.shape[2]):
    img = projects[:,:,i]

    avg_fft = np.zeros(64)
    for w in range(img.shape[1]-64):
        for h in range(img.shape[0]):
            vec = img[h,w:w+64]
            avg_fft += np.abs(fft(vec))
    avg_fft /= ((img.shape[0]-64)*img.shape[1])
    total_fft += avg_fft

plt.plot(range(3,32),total_fft[3:32])

print(avg_fft)