# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:04:19 2017

@author: Vision
"""

from PIL import Image
from skimage.feature import hessian_matrix
from pylab import *
import matplotlib.pyplot as plt

img = array(Image.open('D:\cv.jpg').convert('L'))
hxx,hxy,hyy = hessian_matrix(img,sigma = 3)
Wdet = hxx * hyy
Wtr = hxy * hxy
hesssiananim = Wdet - Wtr
min_dist = 10
threshold = 0.1
corrner_threshold = hesssiananim.max() * threshold
hessiananim_t = (hesssiananim > corrner_threshold)
coords = array(hessiananim_t.nonzero()).T
candidate_values = [hesssiananim[c[0],c[1]] for c in coords]
index = argsort(candidate_values)
allowed_locations = zeros(hesssiananim.shape)
allowed_locations[min_dist:-min_dist,min_dist:-min_dist] = 1
filtered_coords = []
for i in index:
    if allowed_locations[coords[i,0],coords[i,1]]==1:
        filtered_coords.append(coords[i])
        allowed_locations[(coords[i,0]-min_dist):(coords[i,0]+min_dist),
                            (coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0
                            
figure()
gray()
imshow(img)
plot([p[1] for p in filtered_coords],
                  [p[0] for p in filtered_coords],'*r')
                  
axis('off')
