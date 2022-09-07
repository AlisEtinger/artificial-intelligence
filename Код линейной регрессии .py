#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


def loadData():
    data = np.loadtxt('dataLinearRegression.txt',delimiter=',')
    n = data.shape[1]-1
    X = data[:,0:n]
    y = data[:,-1].reshape(-1,1)
    return X,y


# In[ ]:


#напишем код наименьших квадратов 


# In[4]:


X_origin,y = loadData()
X = np.insert(X_origin,0,values=1,axis=1)


# In[ ]:


theta = np.linalg.inx(X.T.dot(X)).dot(X.T).dot(y)


# In[5]:


import matplotlib.pyplot as plt
plt.scatter(X_origin,y)
h_theta = theta[0]+theta[1]*X_origin
plt.plot(X_origin,h_theta)
plt.show()


# In[ ]:


#В этом разделе в основном реализуется код метода наименьших квадратов
#Следует отметить, что когда распределение данных очень отличается, данные необходимо нормализовать.

