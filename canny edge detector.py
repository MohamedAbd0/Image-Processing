# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 18:10:33 2017

@author: Vision
"""

from scipy import ndimage as ndi
from skimage import feature
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = ndi.rotate(im,15)
im += 0.2*np.random.random(im.shape)
fig,(ax1,ax2,ax3) = plt.subplots(nrows=1,ncols=3)
ax1.imshow(im,cmap=plt.cm.gray)
edge1 = feature.canny(im)
edge2 = feature.canny(im,3)
ax2.imshow(edge1,cmap=plt.cm.gray)
ax3.imshow(edge2,cmap=plt.cm.gray)

