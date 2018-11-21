#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np


# In[29]:


def my_product_two_dim_with_threshold(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def get_my_data():
    my_data_x=[]
    my_data_x.append([1,0,0])
    my_data_x.append([1,0,1])
    my_data_x.append([1,1,0])
    my_data_x.append([1,1,1])
    my_data_x
    
    my_data_y=[]
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(1)
    my_data_y
    
    return my_data_x,my_data_y


# In[30]:


x,y=get_my_data()

for a,b in zip(my_data_x,my_data_y):
    print(a,b)
    


# In[31]:


def get_parameters():    
    w=[]
    w.append(3)
    w.append(2)                                            #random
    w.append(1)
    w
    learning_rate=1
    epoch=100                                              #random
 
    return w, learning_rate, epoch


# In[32]:


w,learning_rate,epoch=get_parameters()
samples,output=get_my_data()


# In[33]:


output


# In[47]:


for i in range (10):              #epoch):
    error="hata_yok"
    s=-1
    print("**************************************")
    for each_sample,d in zip(samples,output):
        print("ağırlık : ", w)
        print("örnek ", each_sample)
        print("gerçek output ",d)
        #print(my_product_two_dim_with_threshold(w, each_sample))
        
        u=my_product_two_dim_with_threshold(each_sample,w)
        #print u
        if(u>0):
            y=1
        else:
            y=0
        print("tahmin çıktı : ", u)
        print("")
        
        if(y!=d):                  #error var
            for s in range(3):
                w[s]=w[s]-learning_rate*(y-d)*each_sample[s]
            error="hata_var"
    if(error=="hata_yok"):
        print("hata yok")
        break                               #return 0
                         


# In[ ]:





# In[ ]:




