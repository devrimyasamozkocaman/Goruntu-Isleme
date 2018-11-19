#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread('images.jpeg')
get_ipython().run_line_magic('matplotlib', 'inline')
plt.imshow(img)


# In[3]:


def tersini_alma(img):
    m,n=img.shape[0], img.shape[1]
    ters_img=img.copy()
    for i in range (m):
        for j in range(n):
            ters_img[i,j,0]=255-img[i,j,0]
            ters_img[i,j,1]=255-img[i,j,1]
            ters_img[i,j,2]=255-img[i,j,2]
    return ters_img

plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(tersini_alma(img))


# In[4]:


def histogram(image_1):
    
    redhistogram={}              
    greenhistogram={}
    bluehistogram={}
    
    for i in range(image_1.shape[0]):
        for j in range(image_1.shape[1]):
            if(image_1[i,j,0]) in redhistogram.keys():
                redhistogram[image_1[i,j,0]]=redhistogram[image_1[i,j,0]]+1
            else:
                redhistogram[image_1[i,j,0]]=1
    for i in range(image_1.shape[0]):
        for j in range(image_1.shape[1]):
            if(image_1[i,j,1]) in greenhistogram.keys():
                greenhistogram[image_1[i,j,1]]=greenhistogram[image_1[i,j,1]]+1
            else:
                greenhistogram[image_1[i,j,1]]=1
                
    for i in range(image_1.shape[0]):
        for j in range(image_1.shape[1]):
            if(image_1[i,j,2]) in bluehistogram.keys():
                bluehistogram[image_1[i,j,2]]=bluehistogram[image_1[i,j,2]]+1
            else:
                bluehistogram[image_1[i,j,2]]=1
    
    return redhistogram, greenhistogram, bluehistogram


# In[5]:


hist1, hist2, hist3=histogram(img)

plt.bar(list(hist1.keys()), list(hist1.values()), color='r')
plt.show()
plt.bar(list(hist2.keys()), list(hist2.values()), color='g')
plt.show()
plt.bar(list(hist3.keys()), list(hist3.values()), color='b')
plt.show()


# In[6]:


def getmean(image):
    m=image.shape[0]
    n=image.shape[1]
    k=m*n                             #toplam pixel sayısı
    toplam=0
    for i in range(m):
        for j in range(n):
            toplam=toplam+(image[i,j,0]+image[i,j,1]+image[i,j,2])/3
    toplam=toplam/k
    return toplam


# In[7]:


getmean(img)


# In[ ]:




