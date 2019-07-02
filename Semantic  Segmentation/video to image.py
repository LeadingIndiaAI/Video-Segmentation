"""
Created on May 10  2019

@author: Gowtham C - Nehal Ram Surya B - Vimal Prasanna K G
"""

'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

'''
import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('Royalty Free Stock Footage of People and Dogs and Cats (link in description).mp4')

try:
    if not os.path.exists(folder): #folder->folname to be created to store the frames
        os.makedirs(folder)
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Saves image of the current frame in jpg file
    name = './folder/frame' + str(currentFrame) + '.jpg' #folder->name of folder created to store the frames
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
print("done")
cap.release()
