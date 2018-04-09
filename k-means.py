# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:47:19 2017

@author: Vision
"""

import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target
estimators = [('k_means_iris_8',KMeans(n_clusters=8)),
              ('k_means_iris_3',KMeans(n_clusters=3)),
              ('k_means_iris_bad_init',KMeans(n_clusters=3,n_init=1,
                                              init='random'))]
fignum = 1
titles = ['8 clusters','3 clusters','3 clusters,bad initialization']
for name,est in estimators:
    fig = plt.figure(fignum,figsize=(4,3))
    ax = Axes3D(fig,rect=[0,0,0.59,1],elev = 48,azim=134)
    est.fit(X)
    labels = est.labels_
    ax.scatter(X[:,3],X[:,0],X[:,2],
               c = labels.astype(np.float),edgecolor='k')
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.zaxis.set_ticklabels([])           
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(titles[fignum-1])
    ax.dist = 10
    fignum = fignum +1
fig.show()                                         