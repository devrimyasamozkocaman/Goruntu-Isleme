#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


data=[]
data.append([[0,0,0],[1,1,0],[1,1,0]])
data.append([[0,1,0],[0,1,0],[0,1,0]])
data.append([[0,0,1],[1,0,0],[1,1,1]])
data.append([[0,1,0],[1,0,0],[1,1,1]])
data.append([[0,1,0],[1,1,0],[1,1,0]])
data.append([[0,1,0],[1,1,1],[1,1,0]])
data.append([[0,1,0],[1,1,1],[1,1,1]])
data.append([[1,1,1],[1,1,1],[1,1,1]])
data.append([[0,0,0],[0,0,0],[0,0,0]])
data.append([[0,0,0],[0,0,1],[0,0,0]])

siniflarimiz={0:1, 1:2, 2:3, 3:2, 4:2, 5:3, 6:2, 7:2, 8:3, 9:1}


# In[3]:


def benzerlik_bul(inp,data):
    sim=0
    for i in range(3):
        for j in range(3):
            sim=sim+inp[i][j]*data[i][j]
    return sim


# In[4]:


def benzerlikleri_bul(inp):
    benzerlik_dizisi=[]
    sayi=len(data)
    for i in range (sayi):
        benzerlik=benzerlik_bul(inp,data[i])
        benzerlik_dizisi.append(benzerlik)
    return benzerlik_dizisi


# In[5]:


def farklari_bul(benzerlik_dizisi):
    farklar=[]
    en_buyuk_b=max(benzerlik_dizisi)
    for i in range(10):
        farklar.append(abs(en_buyuk_b-benzerlik_dizisi[i]))
    return farklar


# In[6]:


def indisleri_bul(farklar, k):
    indisler=[]
    ksayac=0
    fark=0
    for j in range (k):
        for i in range(10):
            if (ksayac!=5):
                if(farklar[i]==fark):
                    indisler.append(i)
                    ksayac=ksayac+1
        fark=fark+1
    return indisler


# In[7]:


def sinifi_bul(indisler, k):
    siniflar=[]
    for i in range (k):
        if (i) in siniflarimiz.keys():
            siniflar.append(siniflarimiz[i])
    return siniflar


# In[10]:


def find_class_with_knn(input, k):
    benzerlik_dizi=benzerlikleri_bul(input)
    farklarr=farklari_bul(benzerlik_dizi)
    indisler=indisleri_bul(farklarr, k)
    siniff_dizi=sinifi_bul(indisler, k)
    class_1=0
    class_2=0
    class_3=0
    for i in range (k):
        if (siniff_dizi[i]==1):
            class_1=class_1+1
        if (siniff_dizi[i]==2):
            class_2=class_2+1
        if (siniff_dizi[i]==3):
            class_3=class_3+1
    if (class_1>class_2 and class_1>class_3):
        myclass=1
    if (class_2>class_1 and class_2>class_3):
        myclass=2
    if (class_3>class_1 and class_3>class_2):
        myclass=3
    return myclass


# In[11]:


sinifsiz=[[0,1,0], [1,1,0], [0,1,1]]
print(find_class_with_knn(sinifsiz,5))


# In[ ]:




