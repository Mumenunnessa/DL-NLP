#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
b = 0.1
w = [0.5, 0.5, 0.5, 0.5]
lr = 0.01


# In[2]:


x = [1, 2, 3]
y = 1.5


# In[3]:


def sum():
    s = x[0]*w[0] + x[1]*w[1] + x[2]*w[2] + b*w[3];
    return s;


# In[4]:


#def activation():
   # s = sum();
    
   # if s>0:
    #    return 1;
    #else:
    #    return 0;    (or,)

def activation():
    s = sum();
    soft = 1 / (1+math.exp(-s));
    if soft>0:
        return 1;
    else: 
        return 0;
    return soft;


# In[5]:


a = activation();
error = y - a;
print("error:",error);
print("activation:", a);


# In[6]:


w[0] = w[0] + error*lr*x[0];
w[1] = w[1] + error*lr*x[1];
w[2] = w[2] + error*lr*x[2];
w[3] = w[3] + error*lr*b;


# In[7]:


print(w[0], w[1], w[2], w[3]);


# In[ ]:




