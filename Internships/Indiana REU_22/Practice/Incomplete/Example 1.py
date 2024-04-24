#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import matplotlib.pyplot as plt


# In[22]:


XS = np.arange(-2.0*np.pi,2.0*np.pi,.01)
print(XS)


# In[23]:


YS = np.sin(XS)
YS


# In[24]:


plt.figure(1)
plt.plot(XS,YS,color = 'c',linewidth = 3, label = 'Sine Function')
plt.grid()
plt.xlabel('X Values', fontsize = 'x-large')
plt.ylabel('Sin(x) Values', fontsize = 'x-large')
plt.title('A Simple Plotting Example', fontsize = 'x-large')


# In[49]:


data = np.loadtxt('/N/u/csalonis/Carbonate/Downloads/scope_1.csv',delimiter=',',skiprows=2)
X = data[:,0]
Y = data[:,1]
X


# In[50]:


Y


# In[48]:


plt.figure(2)
plt.plot(X,Y,color = 'b',lw = 1.5, ls =':')
plt.grid()
plt.show()


# In[ ]:




