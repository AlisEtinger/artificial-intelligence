#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split


# In[6]:


data = np.genfromtxt ('linear.csv', delimiter=',')
plt.scatter(data[1:,0],data[1:,1]) 


# In[8]:


x.Train,xTest,yTrain,yTest = train_test_split(data[1:,0],data[1:,1],test_size=0.3)


# In[9]:


x.Train = x.Train[:, np.newaxis]
x.Test = x.Test[:, np.newaxis] 


# In[10]:


model = LinearRegression
model.fit(xTrain,yTrain)


# In[11]:


plt.scatter(x.Train, y.Train, color='y')
plt.scatter(x.Train, y.Train, color='b')


# In[12]:


plt.plot(x.Test, model.predict(x.Test), color='r', linewidth=5)
plt.title('Age vs Quality')
plt.xlabel('Age')
plt.ylabel('Quality')
plt.show


# In[ ]:




