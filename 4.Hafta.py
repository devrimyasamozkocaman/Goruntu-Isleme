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


def get_distance (v):
    w=[1/3,1/3,1/3]
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


# In[4]:


def convert_rgbtogray(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    graypic=np.zeros((m,n))
    for i in range (m):
        for j in range(n):
            graypic[i,j]=get_distance(im_1[i,j,:])
    return graypic


# In[5]:


gray_pic=convert_rgbtogray(img)

plt.subplot(1,2,1),plt.imshow(img)                      #görüntünün işlemsiz hali
plt.subplot(1,2,2),plt.imshow(gray_pic, cmap='gray')    #görüntünün gray level hali


# In[6]:


def graylevel_to_blackwhite(image_graylevel, threshold):       #fonksiyona parametre olarak bir eşik değeri gönderilmeli                                                            #parametre olarak gönderilen görüntü gray level formatta olmalı
    m,n = (image_graylevel.shape[0], image_graylevel.shape[1])
    image_blackwhite = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if (image_graylevel[i,j] > threshold):
                image_blackwhite[i,j] = 1
            else:
                image_blackwhite[i,j] = 0
    return image_blackwhite

image_blackwhite = graylevel_to_blackwhite(gray_pic, 125)
plt.subplot(1,3,1),plt.imshow(img)                             #görüntünün işlemsiz hali
plt.subplot(1,3,2),plt.imshow(gray_pic, cmap='gray')           #görüntünün gray level hali
plt.subplot(1,3,3),plt.imshow(image_blackwhite, cmap='gray')   #görüntünün siyah-beyaz hali


# In[ ]:




