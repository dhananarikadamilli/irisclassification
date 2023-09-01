#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # cleaning the data

# In[2]:


df = pd.read_csv("C:/Users/DHANALAKSHMI/Downloads/archive/IRIS.csv")
df.head()


# In[11]:


df.tail()


# In[12]:


df.describe()


# In[3]:


df.info()


# In[4]:


df['species'].value_counts()


# In[5]:


df['species']=df['species'].str.replace('Iris-','')


# In[6]:


df['species'].value_counts()


# In[7]:


missing_values = df.isnull().sum()
percentage_missing = (missing_values/len(df))*100
pd.DataFrame({'missing_values': missing_values,'percentage_missing': percentage_missing})


# # Data Visualization

# In[9]:


green_palette = sns.color_palette("viridis", n_colors=3)
sns.pairplot(df,hue='species',palette=green_palette)
plt.show()


# In[10]:


num_columns = list(df.select_dtypes(include=['float']).columns)
num=int(len(num_columns)/2) if int(len(num_columns)/2)>1 else 2
fig ,ax = plt.subplots(num,num,figsize=(12,10))
for j in range(num):
    for i in range(num):
        try:
            sns.histplot(data=df,x=num_columns[0],kde=True,bins=20,hue='species',ax=ax[j][i])
            num_columns.pop(0)
        except:
            fig.delaxes(ax=ax[j][i])
fig.suptitle('Histograms of features', fontsize=16)
plt.show()


# In[ ]:




