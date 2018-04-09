# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:23:45 2017

@author: Vision
"""

from skimage.transform import (hough_line,hough_line_peaks)
import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((100,100))

index = np.arange(25,75)

image[index[::-1],index]=255
image[index,index]=255
h,theta,d=hough_line(image)

fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(8,8))
ax1.imshow(image,cmap=plt.cm.gray)
ax1.set_title('input image')
ax1.set_axis_off()

ax2.imshow(h,cmap=plt.cm.gray)
ax2.set_title('Hough Transform')
ax2.set_axis_off()

ax1.imshow(image,cmap=plt.cm.gray)
rows,cols=image.shape

for _,angle,dist in zip(*hough_line_peaks(h,theta,d)):
    y0 = (dist-0*np.cos(angle))/np.sin(angle)
    y1 = (dist-cols*np.cos(angle))/np.sin(angle)
    ax3.plot((0,cols),(y0,y1),'-r')
    
ax3.set_title('Detected Lines')
ax3.set_axis_off()

















