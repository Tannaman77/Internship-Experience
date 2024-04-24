#!/usr/bin/env python
# coding: utf-8

# In[162]:


#The updated, most accurate version of Pulse Finder by Cornelius 


# In[163]:


from matplotlib import pyplot
import numpy as np
Waveforms = np.loadtxt('/N/u/csalonis/Carbonate/Downloads/Run0002.csv')



# In[ ]:




# In[194]:


#Creates the lists for which the voltage and time trigger points for each waveform will be saved onto
SavedVolt = []
SavedTime = []


# In[195]:


#Creates a list, T, that will act as the x axis that goes up to 4 nano seconds
#The second part is the for loop which will set the trigger value k for all waveforms, find the (x,y) or (T,V) points for each waveform in range
#After it finds the T and V points it will append that data to SavedTime and SavedVolt
T = np.array(range(1,501,1))
XTime = T*(4e-9/500)
for i in range(400):
	Ywave = Waveforms[i,:]
	k = 2090
	Xms = []
	Trigger = False
	Pulse = []
	VMin = []
	XM = 0
    
	for i,(x,y) in enumerate(zip(XTime, Ywave)):
		if y < k and Trigger == False:
			Trigger = True
			Pulse.append(x)
			XM = y
            
	elif Trigger == True and y < XM:
		XM = y
               
	elif y > k and Trigger == True:
		Trigger = False
		Xms.append(XM)
	else:
 		pass
	for x in Xms:
		SavedVolt.append(x)
	for y in Pulse:
		SavedTime.append(y)
        


# In[196]:


#Converts SavedVolt and SavedTime to an array
ASV = np.array(SavedVolt)
AST = np.array(SavedTime)
ASV2 = 2100 - ASV


# In[197]:


SavedTime


# In[ ]:





# In[198]:


#Plots the last graph in range to make sure everything is adding up
pyplot.figure(1)
pyplot.plot(XTime, Ywave, lw = 2, c = 'g', ls = ':')
pyplot.axhline(y = k, xmin = 0, xmax =1,c = 'r')
pyplot.scatter(Pulse,Xms,c='b')
pyplot.grid()
pyplot.show()


# In[202]:


#Plots the minimum voltage points on a histogram
pyplot.hist(ASV2, bins = 30, range= (0,30))
pyplot.xlabel('Amplitude')
pyplot.ylabel('Pulse Count')


# In[ ]:




