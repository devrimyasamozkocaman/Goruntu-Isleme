#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread('images.jpeg')
get_ipython().run_line_magic('matplotlib', 'inline')
plt.imshow(img)


# In[15]:


def get_distance (v):
    w=[1/3,1/3,1/3]
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


# In[16]:


def convert_rgbtogray(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    graypic=np.zeros((m,n))
    for i in range (m):
        for j in range(n):
            graypic[i,j]=get_distance(im_1[i,j,:])
    return graypic


# In[17]:


gray_pic=convert_rgbtogray(img)


# In[18]:


def get_median(poi):
    array = poi.reshape(1,9)       #matrisi 1 satır ve 9 sütundan oluşacak şekilde yeniden boyutlandırma
    array.sort()
    return array[0,4]              #median(ortanca) değerini döndürme


# In[19]:


def get_median_filter(image):    #parametre olarak alınan görüntünün gray level olması gerekli
    m = image.shape[0]
    n = image.shape[1]
    
    image_median = np.zeros((m,n))

    for i in range(1, m-1):      #taşmaları engellemek için sınır değerleri 1 ve m-1 olmalı
        for j in range(1, n-1):
            poi = image[i-1:i+2, j-1:j+2]
            image_median[i,j] = get_median(poi)     
    return image_median


# In[20]:


image_median_filtered = get_median_filter(gray_pic)
plt.subplot(1,2,1),plt.imshow(gray_pic, cmap='gray')                 #görüntünün gray level hali
plt.subplot(1,2,2),plt.imshow(image_median_filtered, cmap='gray')    #görüntünün median filtresi uygulandıktan sonraki hali


# In[21]:


def get_default_mask_for_mean():                                     #maske
    return np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3) / 9
    
def apply_mask(part_of_image, mask = get_default_mask_for_mean()):   #maskeleme işleminin yapıldığı fonksiyon
    return sum(sum(part_of_image * mask))


# In[22]:


def get_mean_filter(image):                                          #parametre olarak gönderilen görüntü gray level olmalı
    m = image.shape[0]
    n = image.shape[1]

    image_mean = np.zeros((m,n))

    for i in range(1, m-1):
        for j in range(1, n-1):
            poi = image[i-1:i+2, j-1:j+2]
            image_mean[i,j] = apply_mask(poi)
            
    return image_mean


# In[23]:


image_mean_filtered = get_mean_filter(gray_pic)


# In[24]:


plt.subplot(1,3,1),plt.imshow(gray_pic, cmap='gray')              #görüntünün gray level hali
plt.subplot(1,3,2),plt.imshow(image_mean_filtered, cmap='gray')   #görüntünün mean filtresi uygulanmış hali
plt.subplot(1,3,3),plt.imshow(image_median_filtered, cmap='gray') #görüntünün median filtresi uygulanmış hali


# In[ ]:




