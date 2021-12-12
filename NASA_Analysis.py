#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import plotly.express as px
from geopy.geocoders import Nominatim
import geopy as gp
from datetime import datetime


# # Data
# 

# In[3]:


data = pd.read_csv('meteorite-landings.csv')
data.head()


# In[4]:


print(data.columns)


# # Data in Detail

# In[5]:


print("Data described: \n")
print(data.describe())
print('\n')
print("Data info: \n")
print(data.info())
print('\n')
print("Data types: \n")
print(data.dtypes)


# In[6]:


data.nametype.value_counts()


# Valid is for most meteorites.
# Relict are for objects that were once meteorites but are now highly altered by weathering on.
# 
# 

# # Data Cleaning

# In[7]:


# Rename Columns
data.rename(columns={'recclass':'class', 'reclat':'lat', 'reclong':'long', 'mass (g)':'mass'}, inplace=True)
data.head()


# # Sampling

# In[8]:


print("Original Data Stats: \n")
print(data.describe())

print('\n--------\n')

print("New Sample Data Stats: \n")
data['year'].fillna(0).astype(int)
data['mass'].fillna(0).astype(int)


data = data.sample(frac=0.1)  # 10% sample set
print(data.describe())


# # Plots

# ###  Fall vs Fallen

# In[9]:


data['fall'].hist(bins=3)  
plt.show()


# ### Top 10 classification of meteors

# In[11]:


top_10_class = data['class'].value_counts()[:10]
plt.bar(top_10_class, height = 1)

top_10_class.plot(kind='bar');


# ### Geolocation Conversion

# In[12]:


geolocator = Nominatim(user_agent="project_impact")

lists = []
for i in range(20):
    lats = data['lat'].get(key = i)
    longs = data['long'].get(key = i)
    coor = gp.Point(lats, longs)
    country = geolocator.reverse(gp.Point(coor)).raw['address'].get('country')
    lists.append(country)
print(lists)


# ### Year vs Mass

# In[13]:


fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(data['year'], data['mass'])
plt.show()


# ### Equator or Poles

# In[16]:


axes = plt.gca()
axes.set_ylim([-90,90])
above_equator = data[data.lat >0].shape[0]
at_equator = data[data.lat ==0].shape[0]
below_equator = data[data.lat <0].shape[0]

print("Above Equator:", above_equator, '\n')
print("At Equator:", at_equator, '\n')
print("Below Equator:", below_equator, '\n')

labels = ["Above", 'At', 'Below']
values = [above_equator, at_equator, below_equator]
plt.pie(values, labels=labels)
plt.show()


# In[ ]:




