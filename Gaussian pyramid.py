# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:46:11 2017

@author: Vision
"""

from PIL import Image
import matplotlib.pyplot as plt
from skimage.transform import  pyramid_gaussian
img = Image.open('D:\VS.jpg')
pyramid = tuple(pyramid_gaussian(img))
fig,(ax1,ax2,ax3,ax4,ax5,ax6,ax7)=plt.subplots(nrows=1,ncols=7,figsize=(10,20))
ax1.imshow(pyramid[0])
ax1.set_axis_off()
ax2.imshow(pyramid[1])
ax2.set_axis_off()
ax3.imshow(pyramid[2])
ax3.set_axis_off()
ax4.imshow(pyramid[3])
ax4.set_axis_off()
ax5.imshow(pyramid[4])
ax5.set_axis_off()
ax6.imshow(pyramid[5])
ax6.set_axis_off()
ax7.imshow(pyramid[6])
ax7.set_axis_off()