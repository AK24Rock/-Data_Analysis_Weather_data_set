#!/usr/bin/env python
# coding: utf-8

# # Working on Real Project with Python 

# # (A part of Big Data Analysis)

# -----

# # The Weather Dataset
# ***
# Here, 
# The Weather Dataset is a time-series data set with per-hour information about the weather conditions at a particular location. It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure, and Conditions.
# 
# 
# This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame.

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("1. Weather Data.csv")


# In[3]:


df


# # How to Analyze DataFrames ?

# # .head()
# It shows the first N rows in the data (by default, N=5).

# In[4]:


df.head()


# # .shape
# 
# It shows the total no. of rows and no. of columns of the dataframe

# In[5]:


df.shape


# # .index
# This attribute provides the index of the dataframe

# In[6]:


df.index


# # .columns
# It shows the name of each column

# In[7]:


df.columns


# # .dtypes
# It shows the data-type of each column 

# In[8]:


df.dtypes


# # .unique()
# In a column, it shows all the unique values. 
# It can be applied on a single column only, not on the whole dataframe.

# In[9]:


df['Weather'].unique()


# # .nunique()
# It shows the total no. of unique values in each column. 
# It can be applied on a single column as well as on whole dataframe.

# In[10]:


df['Weather'].nunique()


# In[11]:


df.nunique()


# # .count 
# It shows the total no. of non-null values in each column. 
# It can be applied on a single column as well as on whole dataframe.

# In[12]:


df['Weather'].count()


# In[13]:


df.count()


# # .value_counts
# In a column, it shows all the unique values with their count. It can be applied on single column only.

# In[14]:


df['Weather'].value_counts()


# # .info()
# Provides basic information about the dataframe.

# In[15]:


df.info()


# -----

# # Q) 1.  Find all the unique 'Wind Speed' values in the data.

# In[16]:


df['Wind Speed_km/h'].unique()


# # Q) 2. Find the number of times when the 'Weather is exactly Clear'.

# In[17]:


df.head()


# In[18]:


df.sample(7)


# In[19]:


df.Weather.value_counts()


# In[20]:


df[df.Weather == 'Clear']


# In[21]:


df.groupby('Weather').get_group('Clear')


# # Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[22]:


df.head(7)


# In[23]:


df.columns


# In[24]:


df[df['Wind Speed_km/h'] == 4]


# # Q. 4) Find out all the Null Values in the data.

# In[25]:


df.isnull().sum()


# In[26]:


df.notnull().sum()


# # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[27]:


df.rename(columns = {'Weather' : 'Weather Condition'} ,inplace = 'True')


# In[28]:


df.head(5)


# # Q.6) What is the mean 'Visibility' ?

# In[29]:


df.Visibility_km.mean()


# # Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# In[30]:


df.Press_kPa.std()


# # Q. 8) Whats is the Variance of 'Relative Humidity' in this data ?

# In[31]:


df['Rel Hum_%'].var()


# # Q. 9) Find all instances when 'Snow' was recorded.

# In[32]:


df.head()


# In[33]:


df['Weather Condition'].value_counts


# In[34]:


df[df['Weather Condition'] == 'Snow']


# # Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[35]:


df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] ==25)]


# # Q. 11) What is the Mean value of each column against each 'Weather Conditon' ?

# In[36]:


df.groupby('Weather Condition').mean()


# # Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Conditon' ?

# In[37]:


df.groupby('Weather Condition').max()


# In[38]:


df.groupby('Weather Condition').min()


# # Q. 13) Show all the Records where Weather Condition is Fog.

# In[39]:


df[df['Weather Condition'] =='Fog']


# # Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[40]:


df[(df['Weather Condition'] =='Clear') | (df['Visibility_km'] > 40)].tail(50)


# # Q. 15) Find all instances when :
# ### A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# ### or
# ### B. 'Visibility is above 40'

# In[41]:


df[(df['Weather Condition'] =='Clear') & (df['Rel Hum_%'] > 50) | (df['Visibility_km'] > 40)]


# ----
