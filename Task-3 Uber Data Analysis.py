#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Project Name:
    
                                     # Uber Data Analysis


# In[ ]:


# Problem Statement:
    # In this problem statement, we will find the days on which each basement has more trips,
    # we will find the days on which each basement has more number of active vehicles.


# In[ ]:


# Importing Libraries


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


# Importing Dataset


# In[3]:


dataset = pd.read_csv("https://raw.githubusercontent.com/goodluck08/practice_dataset/main/uberdrive.csv")
dataset.head()


# In[ ]:


# To find the shape of the dataset


# In[4]:


dataset.shape


# In[ ]:


#  To Print the description of data


# In[5]:


dataset.describe()


# In[ ]:


# To check the info of the data


# In[6]:


dataset.info()


# In[ ]:


# Data Preprocessing
       # As we understood that there are a lot of null values in PURPOSE column,
      # so for that we will me filling the null values with a NOT keyword. You can try something else too.


# In[15]:


dataset["PURPOSE*"].fillna("NOT", inplace=True)


# In[16]:


dataset["PURPOSE*"]


# In[ ]:


# Changing the START_DATE and END_DATE to the date_time format so that further it can be use to do analysis.


# In[17]:


dataset["START_DATE*"] = pd.to_datetime(dataset["START_DATE*"],
                                       errors='coerce')
dataset["END_DATE*"] = pd.to_datetime(dataset["END_DATE*"],
                                     errors='coerce')


# In[18]:


dataset["START_DATE*"]


# In[19]:


dataset["END_DATE*"]


# In[ ]:


# Splitting the START_DATE to date and time column and then converting the time into four different categories 
            # i.e. Morning, Afternoon, Evening, Night


# In[20]:


from datetime import datetime
 
dataset['date'] = pd.DatetimeIndex(dataset['START_DATE*']).date
dataset['time'] = pd.DatetimeIndex(dataset['START_DATE*']).hour
 
#changing into categories of day and night
dataset['day-night'] = pd.cut(x=dataset['time'],
                              bins = [0,10,15,19,24],
                              labels = ['Morning','Afternoon','Evening','Night'])


# In[21]:


dataset['day-night']


# In[22]:


# Once we are done with creating new columns, we can now drop rows with null values.


# In[23]:


dataset.dropna(inplace=True)


# In[24]:


# It is also important to drop the duplicates rows from the dataset. To do that, refer the code below.


# In[25]:


dataset.drop_duplicates(inplace=True)


# In[ ]:


# Data Visualization
        # In this section, we will try to understand and compare all columns.
       # Let’s start with checking the unique values in dataset of the columns with object datatype.


# In[26]:


obj = (dataset.dtypes == 'object')
object_cols = list(obj[obj].index)
 
unique_values = {}
for col in object_cols:
  unique_values[col] = dataset[col].unique().size
unique_values


# In[ ]:


# Now, we will be using matplotlib and seaborn library   


# In[ ]:


# Plot a bar graph for purposes VS Distance.


# In[43]:


df=pd.DataFrame(dataset["MILES*"].groupby(dataset["PURPOSE*"]).sum())
df.plot(kind='bar')
plt.show()


# In[ ]:


# OR


# In[46]:


df=df.reset_index()
sns.barplot(x=df["MILES*"],y=df["PURPOSE*"])


# In[ ]:


# Print the data frame of purposes and the distance travelled for that particular purpose.


# In[47]:


df


# In[ ]:


# Plot number of trips VS category of trips.


# In[48]:


dataset.head()
df=pd.DataFrame(dataset["CATEGORY*"].value_counts())
df.reset_index()
df.plot(kind='bar')
plt.show()
df


# In[49]:


# Proportion of trips for business & proportion of trips for personal.


# In[51]:


df=dataset.groupby(["CATEGORY*"]).sum()
Business=df.iloc[0,0]/(df.iloc[0,0]+df.iloc[1,0])
Personal=df.iloc[1,0]/(df.iloc[0,0]+df.iloc[1,0])

print('Business',Business)
print('Personal',Personal)


# In[ ]:


#--------------THE-END--------------#   
    
    

