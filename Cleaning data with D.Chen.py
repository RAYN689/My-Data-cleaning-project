#!/usr/bin/env python
# coding: utf-8

# In[98]:


import pandas as pd


# In[30]:


weather_file = '/Users/olayinkafaniran/Documents/IT PROJECTS/pydatadc_2018-tidy-master/data/weather.csv'
billboard_file = '/Users/olayinkafaniran/Documents/IT PROJECTS/pydatadc_2018-tidy-master/data/billboard.csv'
ebola_file = '/Users/olayinkafaniran/Documents/IT PROJECTS/pydatadc_2018-tidy-master/data/country_timeseries.csv'
file = '/Users/olayinkafaniran/Documents/IT PROJECTS/pydatadc_2018-tidy-master/data/pew.csv'
pew = pd.read_csv(file)


# In[3]:


pew.head()


# In[4]:


pew.shape


# In[5]:


pew_long = pd.melt(pew, id_vars = 'religion')
pew_long.head()


# In[6]:


pew_long = pd.melt(pew, id_vars = 'religion', var_name = 'income', value_name = 'count')
pew_long.head()


# In[7]:


billboard = pd.read_csv(billboard_file)
billboard.head()


# In[8]:


billboard_long = pd.melt(billboard,
        id_vars = ['year','artist','track', 'time', 'date.entered'],
        var_name = 'Week',
        value_name = 'Ratings'
)

billboard_long.head()


# In[9]:


billboard.shape


# In[10]:


billboard_long.shape


# In[11]:


ebola = pd.read_csv(ebola_file)
ebola.head()


# In[12]:


ebola.shape


# In[13]:


ebola_long = pd.melt(ebola,
                     id_vars = ['Date','Day'])
ebola_long.head()


# In[14]:


'Cases_Guinea'.split('_')


# In[15]:


ebola_split = ebola_long['variable'].str.split('_')
ebola_split


# In[16]:


ebola_split[0]


# In[17]:


type(ebola_split[0][0])


# In[18]:


ebola_long['Stats'] = ebola_split.str.get(0)
ebola_long['Country'] = ebola_split.str.get(1)


# In[19]:


ebola_long.head()


# In[33]:


weather = pd.read_csv(weather_file)
weather.head()


# In[46]:


weather_melt = pd.melt(weather, 
                       id_vars = ['id', 'year', 'month', 'element'],
                       var_name = 'Days',
                       value_name = 'temp'
                      )
weather_melt.head()


# In[49]:


weather_tidy = weather_melt.pivot_table(index = ['id', 'year', 'month', 'Days'],
                                        columns = 'element',
                                        values = 'temp'
                                       )
weather_tidy.head()


# In[56]:


weather_tidy.reset_index()


# In[57]:


billboard.head()


# In[59]:


billboard_long.head()                       


# In[82]:


billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
billboard_songs.head()


# In[83]:


billboard_songs.shape


# In[86]:


billboard_songs.loc[billboard_songs['track'] == 'Loser']


# In[87]:


billboard_songs = billboard_songs.drop_duplicates()


# In[88]:


billboard_songs.shape


# In[93]:


billboard_songs['id'] = range(len(billboard_songs))


# In[94]:


billboard_songs.head()


# In[97]:


billboard_songs.to_csv('billboard_newsongs.csv', index = 'False')


# In[ ]:




