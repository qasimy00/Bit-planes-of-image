#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
from PIL import Image as Im


# In[2]:

#Give path of image
im=cv2.imread(r"C:\Users\HP\Downloads\Gris.jpg")


# In[20]:
#Function that takes array of images and makes a gif 
def makegif(array,gifname,durationgif=50):
    a=array
    if type(a[0]!='PIL.Image.Image'):
        for i in range(len(a)):
            a[i] = cv2.cvtColor(a[i], cv2.COLOR_BGR2RGB) 
            a[i] = Im.fromarray(a[i]) 
        a[0].save(gifname,
                    save_all=True, append_images=a[1:], optimize=False, duration=durationgif, loop=0)
    b=a

#SLICE INTO 8 PLANES
planes=[]
for i in range(8):
    planes.append(im & (1 << i))
makegif(planes,'bitplanes.gif',1000)


# In[18]:


#BUILD IMAGE BIT BY BIT
cons=[]
for i in range(8):
    cons.append(im & (1 << i))
    if i>0:
        cons[-1]=cons[-1]+cons[-2]
makegif(cons,'buildbitplanes.gif',1000)

# In[11]:


#GAUSSIANBLUR GIF
blurs=[]
for i in range(1,50,2):
    blurs.append(cv2.GaussianBlur(im,(i,i),0))
blurs.extend(blurs[::-1])
for i in range(3):
    blurs.append(blurs[-1])

makegif(blurs,'gaussianblur.gif',50)



#BLUR GIF
blurs=[]
for i in range(1,50,2):
    blurs.append(cv2.blur(im,(i,i)))
blurs.extend(blurs[::-1])
for i in range(3):blurs.append(blurs[-1])
makegif(blurs,'blur.gif',50)
