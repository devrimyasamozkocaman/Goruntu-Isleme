#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread('images.jpeg')
get_ipython().run_line_magic('matplotlib', 'inline')
plt.imshow(img)


# In[2]:


def boyut_maxmindegerler(my_img):
    print("Eksen sayısı: ", my_img.ndim)
    print("Eksen degeri: ", my_img.shape)
    print("En küçük kırmızı renk degeri: ",np.min(my_img[:,:,0]))
    print("En büyük kırmızı renk degeri: ",np.max(my_img[:,:,0]))
    print("En küçük yeşil renk degeri: ",np.min(my_img[:,:,1]))
    print("En büyük yeşil renk degeri: ",np.max(my_img[:,:,1]))
    print("En küçük mavi renk degeri: ",np.min(my_img[:,:,2]))
    print("En büyük mavi renk degeri: ",np.max(my_img[:,:,2]))


# In[ ]:




