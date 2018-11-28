#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math


# In[2]:


data=[]
data.append([5.1,3.5,1.4,0.2, "setosa"])
data.append([4.9,3.0,1.4,0.2, "setosa"])
data.append([4.7,3.2,1.3,0.2, "setosa"])
data.append([4.6,3.1,1.5,0.2, "setosa"])
data.append([6.4,3.2,4.5,1.5, "versicolor"])
data.append([6.9,3.1,4.9,1.5, "versicolor"])
data.append([5.5,2.3,4.0,1.3, "versicolor"])
data.append([6.5,2.8,4.6,1.5, "versicolor"])
data.append([7.1,3.0,5.9,2.1, "virginica"])
data.append([7.6,3.0,6.6,2.1, "virginica"])
data.append([7.3,2.9,6.3,1.8, "virginica"])
data.append([6.5,3.0,5.8,2.2, "virginica"])


# In[3]:


def uzaklik_hesap(inp,data):
    uzaklik=0
    for i in range(4):
            uzaklik=uzaklik+((inp[i]-data[i])**2)
            uzaklik=uzaklik**.5
    return uzaklik


# In[4]:


def uzakliklari_bul(inp):
    benzerlik_dizisi1=[]
    sayi=len(data)
    for i in range (sayi):
        benzerlik=uzaklik_hesap(inp,data[i])
        benzerlik_dizisi1.append(benzerlik)
    return benzerlik_dizisi1


# In[5]:


def siniflari_bul(benzerlik_dizisi, k):
    siniflar=[]
    yedek=[]
    for i in range (12):
        yedek.append(benzerlik_dizisi[i])
    ksayac=0
    
    for j in range (k):
        for i in range (12):
            if (ksayac!=k):
                if(benzerlik_dizisi[i]==min(yedek)):
                    siniflar.append(data[i][4])
                    print(i)
                    ksayac=ksayac+1
                    yedek.remove(min(yedek))
    return siniflar


# In[6]:


def with_knn_find_class(input, k):
    benzerlik_dizi=uzakliklari_bul(input)
    print(benzerlik_dizi)
    siniflar=siniflari_bul(benzerlik_dizi,k)
    print(siniflar)
    class_1=0
    class_2=0
    class_3=0
    for i in range (k):
        if (siniflar[i]=="setosa"):
            class_1=class_1+1
        if (siniflar[i]=="versicolor"):
            class_2=class_2+1
        if (siniflar[i]=="virginica"):
            class_3=class_3+1
    if (class_1>class_2 and class_1>class_3):
        myclass="setosa"
    if (class_2>class_1 and class_2>class_3):
        myclass="versicolor"
    if (class_3>class_1 and class_3>class_2):
        myclass="virginica"
    return myclass


# In[7]:


sinifsiz=[6.4,3.2,4.5,1.5]
print(with_knn_find_class(sinifsiz,3))


# In[ ]:




