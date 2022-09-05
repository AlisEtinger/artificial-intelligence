#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))


# In[15]:


from scipy import sparse
eye = np.eye(4)
print("\n{}".format(eye))


# In[16]:


sparse_matrix = sparse.csr_matrix(eye)
print("\n{}".format(sparse_matrix))


# In[37]:


data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices))) 
print("\n{}".format(eye_coo))


# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.sin(x)


# In[19]:


import pandas as pd
data = {'Name': ["John", "Anna", "Peter", "Linda"],
'Location' : ["New York", "Paris", "Berlin", "London"], 'Age' : [24, 13, 53, 33]
}
data_pandas = pd.DataFrame(data)
display(data_pandas)


# In[20]:


display(data_pandas[data_pandas.Age > 30])


# In[21]:


import sys
print("{}".format(sys.version))
import pandas as pd
print("{}".format(pd.__version__))
import matplotlib
print("{}".format(matplotlib.__version__))
import numpy as np
print("{}".format(np.__version__))
import scipy as sp
print("{}".format(sp.__version__))
import IPython
print("{}".format(IPython.__version__))
import sklearn
print("{}".format(sklearn.__version__))


# In[40]:


from sklearn.datasets import load_iris 
iris_dataset = load_iris()


# In[41]:


print("Ключи iris_dataset: \n{}".format(iris_dataset.keys()))


# In[42]:


print(iris_dataset['DESCR'][:193] + "\n...")


# In[43]:


print("Названия ответов: {}".format(iris_dataset['target_names']))


# In[44]:


print("Названия признаков: \n{}".format(iris_dataset['feature_names']))


# In[45]:


print("Тип массива data: {}".format(type(iris_dataset['data'])))


# In[46]:


print("Форма массива data: {}".format(iris_dataset['data'].shape))


# In[47]:


print("Первые пять строк массива data:\n{}".format(iris_dataset['data'][:5]))


# In[48]:


print("Тип массива target: {}".format(type(iris_dataset['target'])))


# In[49]:


print("Форма массива target: {}".format(iris_dataset['target'].shape))


# In[50]:


print("Ответы:\n{}".format(iris_dataset['target']))


# In[51]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)


# In[52]:


print("форма массива X_train: {}".format(X_train.shape))
print("форма массива y_train: {}".format(y_train.shape))


# In[53]:


print("форма массива X_test: {}".format(X_test.shape)) 
print("форма массива y_test: {}".format(y_test.shape))


# In[54]:


iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                        hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




