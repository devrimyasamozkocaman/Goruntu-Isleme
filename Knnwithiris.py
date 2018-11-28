#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math


# In[3]:


data=[]
data.append([5.1,3.5,1.4,0.2])
data.append([4.9,3.0,1.4,0.2])
data.append([4.7,3.2,1.3,0.2])
data.append([4.6,3.1,1.5,0.2])
data.append([6.4,3.2,4.5,1.5])
data.append([6.9,3.1,4.9,1.5])
data.append([5.5,2.3,4.0,1.3])
data.append([6.5,2.8,4.6,1.5])
data.append([7.1,3.0,5.9,2.1])
data.append([7.6,3.0,6.6,2.1])
data.append([7.3,2.9,6.3,1.8])
data.append([6.5,3.0,5.8,2.2])

siniflarimiz={0:"setosa", 1:"setosa", 2:"setosa", 3:"setosa", 4:"versicolor", 5:"versicolor", 6:"versicolor", 7:"versicolor", 8:"virginica", 9:"virginica", 10:"virginica", 11:"virginica"}


# In[4]:


def uzaklik_hesap(inp,data):
    uzaklik=0
    for i in range(4):
            uzaklik=uzaklik+((inp[i]-data[i])**2)
            uzaklik=uzaklik**.5
    return uzaklik


# In[5]:


def uzakliklari_bul(inp):
    benzerlik_dizisi1=[]
    sayi=len(data)
    for i in range (sayi):
        benzerlik=uzaklik_hesap(inp,data[i])
        benzerlik_dizisi1.append(benzerlik)
    return benzerlik_dizisi1


# In[6]:


def indisleri_bul(benzerlik_dizisi, k):
    indisler=[]
    yedek=[]
    for i in range (12):
        yedek.append(benzerlik_dizisi[i])
    ksayac=0
    
    for j in range (k):
        for i in range (12):
            if (ksayac!=k):
                if(benzerlik_dizisi[i]==min(yedek)):
                    indisler.append(i)
                    ksayac=ksayac+1
                    yedek.remove(min(yedek))
    return indisler


# In[7]:


def sinifi_bul(indisler, k):
    siniflar=[]
    for i in range (k):
        sayi=indisler[i]
        if (sayi) in siniflarimiz.keys():
            print(siniflarimiz[sayi])
            siniflar.append(siniflarimiz[sayi])
            
    return siniflar


# In[8]:


def with_knn_find_class(input, k):
    benzerlik_dizi=uzakliklari_bul(input)
    print(benzerlik_dizi)
    indisler=indisleri_bul(benzerlik_dizi,k)
    print(indisler)
    siniff_dizi=sinifi_bul(indisler, k)
    print(siniff_dizi)
    class_1=0
    class_2=0
    class_3=0
    for i in range (k):
        if (siniff_dizi[i]=="setosa"):
            class_1=class_1+1
        if (siniff_dizi[i]=="versicolor"):
            class_2=class_2+1
        if (siniff_dizi[i]=="virginica"):
            class_3=class_3+1
    if (class_1>class_2 and class_1>class_3):
        myclass="setosa"
    if (class_2>class_1 and class_2>class_3):
        myclass="versicolor"
    if (class_3>class_1 and class_3>class_2):
        myclass="virginica"
    return myclass


# In[9]:


sinifsiz=[5.4,3.9,1.7,0.4]
print(with_knn_find_class(sinifsiz,3))


# In[ ]:




