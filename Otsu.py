# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 00:36:47 2017

@author: Vision
"""

import matplotlib.pyplot as plt 
from skimage import data
from skimage import filters
from skimage import exposure

camera = data.camera()
val = filters.threshold_otsu(camera)
hist,bins_center = exposure.histogram(camera)
plt.figure(figsize=(9,4))
plt.subplot(131)
plt.imshow(camera,cmap='gray',interpolation='nearest')
plt.axis('off')
plt.subplot(132)
plt.imshow(camera < val,cmap='gray',interpolation='nearest')
plt.axis('off')
plt.subplot(133)
plt.plot(bins_center,hist,lw=2)
plt.axvline(val,color='k',ls='--')

plt.tight_layout()
plt.show()

  
  