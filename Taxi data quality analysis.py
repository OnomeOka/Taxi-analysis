#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use("ggplot")
get_ipython().run_line_magic('matplotlib', 'inline')
from mpl_toolkits.mplot3d import Axes3D
import datetime as dt
import plotly.graph_objects as go
import plotly.express as px


# In[2]:


df = pd.read_csv('Taxi Datset.csv')


# In[4]:


df.head()


# In[6]:


df.isnull().sum()


# In[8]:


df.duplicated()


# In[11]:


#Check for outliers in numerical columns
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for col in numerical_columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    if len(outliers) > 0:
        print(f"\noutliers in {col}:")
        print(outliers)


# In[14]:


# check for inconsistencies in categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    print(f"\nunique values in {col}:")
    print(df[col].unique())


# In[15]:


numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns


# In[16]:


# Create a boxplot for each numerical column
for col in numerical_columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot for {col}')
    plt.show()


# In[18]:


# Create a scatter plot for each numerical column
for col in numerical_columns:
    plt.figure(figsize=(8, 6))
    plt.scatter(df.index, df[col])
    plt.title(f'Scatter plot for {col}')
    plt.xlabel('Index')
    plt.ylabel(col)
    plt.show()


# In[ ]:




