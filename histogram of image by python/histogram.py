from PIL import Image
from pylab import *
import matplotlib.pyplot as plt
x=Image.open('C:/Users/moham/Desktop/lena.jpg').convert('L')
r=array(x)
col = len(r)
row = len(r[0])
hist = { }
# fincton to chick tne number 
def ch_key ( key ):
    for k in hist.keys() :
        if k== key :
            return True
    return False 
#to enter tne num into disc
i=0
while col > i :
    j=0
    while row > j :
        if ch_key(r[i,j])==False:   
            hist[r[i,j]]=1
        else :
            hist[r[i,j]]=hist[r[i,j]]+1
            j=j+1
    i=i+1
plt.subplot(2,1,1),plt.imshow(r,cmap='gray')
plt.subplot(2,1,2), plt.bar(hist.keys(),hist.values(), facecolor='#9999ff', edgecolor='white')
plt.xlabel('The Value Of Pixel')
plt.ylabel('The Number Of Pixel')
plt.title('Histogram of Photo ')


    