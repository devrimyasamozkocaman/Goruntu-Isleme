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


# In[11]:


def create_matris():                            #28x28'lik elemanları 1 ve 0lardan oluşan random matris üreten fonksiyon
    a = np.random.randint(2, size=28*28)
    return a.reshape(28,28)

matris28by28 = create_matris()
print(matris28by28)


# In[12]:


def MBR_olustur(matris1):
    m = matris1.shape[0]
    n = matris1.shape[1]
    x_min=m
    x_max=0                                      #başlangıç değerlerine olası en kötü durum yazılır
    y_min=n
    y_max=0
    
    for i in range(m):
        for j in range(n):
            if(matris1[i,j]==1 and x_min > i):    
                x_min = i                   
            if(matris1[i,j]==1 and x_max < i):
                x_max = i
            if(matris1[i,j]==1 and y_min > j):
                y_min = j
            if(matris1[i,j]==1 and y_max < j):
                y_max = j
    return (x_min,x_max,y_min,y_max)


# In[13]:


MBR_olustur(matris28by28)


# In[14]:


def benzerlik_bul(a,b):
    m,n=a.shape[0], a.shape[1]
    sim=0
    for i in range(m):
        for j in range(n):
            sim=sim+a[i,j]*b[i,j]
    return sim


# In[15]:


c=create_matris()
d=create_matris()
c_dbenzerlik=benzerlik_bul(c,d)
print(c_dbenzerlik)
c_cbenzerlik=benzerlik_bul(c,c)
print(c_cbenzerlik)


# In[16]:


def sim_100():
    matrisler=[]
    for i in range(100):
        yeni_matris=create_matris()
        matrisler.append(yeni_matris)
    for i in range(100):
        benzerlikson=benzerlik_bul(matrisler[0],matrisler[i])
        print('', str(i), '', benzerlikson, end='-')


# In[17]:


sim_100()


# In[ ]:




