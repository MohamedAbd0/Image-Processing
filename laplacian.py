# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:40:09 2017

@author: Vision
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:\cv.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(gray,(3,3),0)

lap = cv2.Laplacian(img,cv2.CV_64F)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('original'),plt.xticks([]),plt.yticks([])

plt.subplot(2,2,2),plt.imshow(lap,cmap='gray')
plt.title('laplacian'),plt.xticks([]),plt.yticks([])