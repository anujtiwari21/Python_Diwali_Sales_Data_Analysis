#!/usr/bin/env python
# coding: utf-8

# In[81]:


#import python libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#import csv file
df = pd.read_csv(r"D:\Softwares\MS Office 2013\admin\Anuj\D_S\Projects\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv",encoding='unicode_escape')


# In[4]:


df


# In[5]:


df.shape


# In[6]:


df.head()


# In[7]:


df.info()


# In[10]:


#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[12]:


#check for null values
df.isnull().sum()


# In[13]:


# drop null values
df.dropna(inplace=True)


# In[15]:


df.isnull().sum()


# In[16]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[17]:


df['Amount']


# In[18]:


df['Amount'].dtypes


# In[19]:


df.columns


# In[21]:


#rename column
df.rename(columns = {'Martial_Status':'Shaadi'})


# In[22]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# In[23]:


# use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# ### Gender

# In[25]:


# plotting a bar chart for Gender and it's count
ax = sns.countplot(x = 'Gender', data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[34]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)


# *From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men*

# ### Age

# In[40]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[44]:


# Total Amount vs Age Group

sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# ### State

# In[54]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index = False) ['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State', y = 'Orders')
plt.show()


# In[55]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# *From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*

# ### Marital Status

# In[58]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc = {'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[62]:


sales_state = df.groupby(['Marital_Status','Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status', y = 'Amount', hue = 'Gender')
plt.show()


# *From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*

# ### Occupation

# In[66]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[70]:


sales_state = df.groupby(['Occupation'],as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending=False)

sns.set(rc = {'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation', y = 'Amount')


# *From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector*

# ### Product Category

# In[73]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[75]:


sales_state = df.groupby(['Product_Category'], as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc = {'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category', y = 'Amount')
plt.show()


# *From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category*

# In[77]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')
plt.show()


# In[79]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.show()


# ## Conclusion:
# 
# ### 

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# complete project on GitHub: https://github.com/anujtiwari21/Python_Diwali_Sales_Data_Analysis

# Thank you!

# In[ ]:




