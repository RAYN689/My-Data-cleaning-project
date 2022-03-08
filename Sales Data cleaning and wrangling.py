#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


test = '/Users/olayinkafaniran/Documents/IT PROJECTS/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/Sales_April_2019.csv'
data = pd.read_csv(test, encoding = 'unicode_escape')


# In[3]:


data.head()


# In[4]:


data.describe()


# In[5]:


data.info()


# In[6]:


data.shape


# In[7]:


#list(data)
data.columns


# In[8]:


data.dtypes


# In[9]:


data.dropna(axis = 'columns', how = 'all')


# In[10]:


data.isnull()


# In[11]:


data


# In[12]:


data[['Quantity Ordered','Price Each', ]].fillna(0)


# In[13]:


data


# In[14]:


type(data.iloc[2,2])


# In[15]:


data.fillna(0)


# In[16]:


#data['Price Each'] = pd.to_numeric(data['Price Each'])
data['Price Each'] = pd.to_numeric(data['Price Each'], errors='coerce')
#data['Price Each'].mean()


# In[17]:


type(data['Price Each'])


# In[18]:


type(data.loc[2,'Price Each'])


# In[19]:


mean_value = round(data['Price Each'].mean(),0)
mean_value


# In[20]:


#data['Price Each'] = data['Price Each'].replace(0, np.nan)
#data.head()


# In[21]:


data['Price Each'] = data['Price Each'].replace(np.nan, mean_value)
data


# In[22]:


data.dropna(axis = 'index', how = 'any')


# In[23]:


data_split = data['Purchase Address'].str.split(',')
data_split.head()


# In[24]:


data['City'] = data_split.str[1]
data['Country'] = data_split.str[2]
data


# In[25]:


data.dropna(axis = 'index', how = 'any', inplace = True)
data


# In[26]:


data_drop = data.drop('Purchase Address', axis = 1)
data_drop.head()


# In[27]:


data_drop[['Order ID','Product']]


# In[28]:


data['Product'].unique()


# In[29]:


filt = (data['Product'] == 'Google Phone')
data[filt]


# In[30]:


new = data.loc[filt, ['Order ID', 'Price Each']]
new


# In[31]:


new2 = (data['Price Each']>600) & (data['Product'] == 'iPhone')
data[new2]


# In[32]:


final = data.loc[new2, ['Product', 'City', 'Price Each']]
final

