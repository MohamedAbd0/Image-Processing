# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 01:19:37 2017

@author: Vision
"""

from __future__ import print_function
import numpy as np
from matplotlib import pyplot as plt
from skimage import data
from skimage.util import img_as_float
from skimage.feature import (corner_harris,corner_subpix,corner_peaks,plot_matches)
from skimage.transform import warp,AffineTransform
from skimage.exposure import rescale_intensity
from skimage.color import rgb2gray
from skimage.measure import ransac

checkerboard = img_as_float(data.checkerboard())
img_orig = np.zeros(list(checkerboard.shape)+[3])
img_orig[...,0] = checkerboard
gradient_r,gradient_c = (np.mgrid[0:img_orig.shape[0],
                                  0:img_orig.shape[1]]
                          / float(img_orig.shape[0]))
img_orig[...,1] = gradient_r
img_orig[...,2] = gradient_c
img_orig = rescale_intensity(img_orig)
img_orig_gray = rgb2gray(img_orig)

tform = AffineTransform(scale=(0.9,0.9),rotation=0.2,translation=(20,-10))
img_wraped = warp(img_orig,tform.inverse,out_shape=(200,200))
img_wraped_gray = rgb2gray(img_wraped)

coords_orig = corner_peaks(corner_harris(img_orig_gray),threshold_rel=0.001,
                                        min_distance=5)
coords_wraped = corner_peaks(corner_harris(img_wraped_gray),threshold_rel=0.001,min_distance=5)

coords_orig_subpix = corner_subpix(img_orig_gray,coords_orig,window_size=9)
coords_wraped_subpix = corner_subpix(img_wraped_gray,coords_wraped,window_size=9)

def gaussian_weights(window_ext,sigma=1):
    y,x = np.mgrid[-window_ext:window_ext+1,-window_ext:window_ext+1]
    g = np.zeros(y.shape,dtype=np.double)
    g[:] = np.exp(-0.5*(x**2/sigma**2+y**2/sigma**2))
    g /= 2*np.pi * sigma * sigma
    return g
def match_corner(coord,window_ext=5):
    r,c = np.round(coord).astype(np.intp)
    window_orig = img_orig[r-window_ext:r+window_ext+1,c-window_ext:c+window_ext+1,:]
    weights = gaussian_weights(window_ext,3)
    weights = np.dstack((weights,weights,weights))
    SSDs = []
    for cr,cc in coords_wraped:
        window_wraped= img_wraped[cr-window_ext:cr+window_ext+1,cc-window_ext:cc+window_ext+1, :]
        SSD = np.sum(weights*(window_orig-window_wraped)**2)
        SSDs.append(SSD)
    min_idx = np.argmin(SSDs)
    return coords_wraped_subpix[min_idx] 

src = []
dst = []
for coord in coords_orig_subpix:
    src.append(coord)
    dst.append(match_corner(coord))
src = np.array(src)
dst = np.array(dst)
model = AffineTransform()
model.estimate(src,dst)

model_robust,inliers = ransac((src,dst),AffineTransform,min_samples=3,
                              residual_threshold=2,max_trials=100)
outliers = inliers == False
 
print(tform.scale,tform.translation,tform.rotation)
print(model.scale,model.translation,model.rotation)
print(model_robust.scale,model_robust.translation,model_robust.rotation)

fig,ax = plt.subplots(nrows=2,ncols=1) 
plt.gray()
inlier_idx = np.nonzero(inliers)[0]
plot_matches(ax[0],img_orig_gray,img_wraped_gray,src,dst,
             np.column_stack((inlier_idx,inlier_idx)),matches_color='b')
ax[0].axis('off')  
ax[0].set_title('correct correspondences') 
outlier_idx = np.nonzero(outliers)[0]
plot_matches(ax[1],img_orig_gray,img_wraped_gray,src,dst,
             np.column_stack((outlier_idx,outlier_idx)),matches_color='r')
ax[1].axis('off')
ax[1].set_title('Faulty correspondences') 
plt.show()








                              