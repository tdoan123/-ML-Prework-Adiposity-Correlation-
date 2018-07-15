
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt


# # Hello World 
# 
# Testing the markdown
# 

# In[10]:


df = pd.read_excel("BodyFat.xls")
df.head(10)


# In[12]:


df["ADIPOSITY"].corr(df["NECK"])


# In[13]:


df["ADIPOSITY"].corr(df["CHEST"])


# In[14]:


df.corr()["ADIPOSITY"]


# In[17]:


plt.matshow(df.corr())


# In[20]:


def plot_corr_with_labels(df):
    corr=df.corr()
    fig, ax= plt.subplots(figsize=(20,20))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)


# In[21]:


plot_corr_with_labels(df)


# In[24]:


under_45 = df[ df["AGE"]<45]
over_45 = df[ df["AGE"]>= 45]

print(under_45.size)
print(over_45.size)


# In[29]:


u45 = under_45.corr()["ADIPOSITY"]
o45 = over_45.corr()["ADIPOSITY"]

for i in range(df.columns.values.size):
    print (u45[i] - o45[i])


# In[31]:


list(df.columns.values)


# ## The characteristic that most strongly correlated with Adiposity is ABDOMEN      0.923880

# ## The characteristic as it relates to predicting someone's adiposity that changes most between people under 45 and people over 45 is: 
# Knee - which changes by .10830842534469676
# 
#     ![](http://jewel925.com/wp-content/uploads/cute-kittens.jpg)
#     
#     
# 

# ![](http://jewel925.com/cat-facts/)
