#!/usr/bin/env python
# coding: utf-8

# In[5]:


# The %... is an iPython thing, and is not part of the Python language.
# In this case we're just telling the plotting library to draw things on
# the notebook, instead of on a separate window.
get_ipython().run_line_magic('matplotlib', 'inline')
#this line above prepares IPython notebook for working with matplotlib

# See all the "as ..." contructs? They're just aliasing the package names.
# That way we can call methods like plt.plot() instead of matplotlib.pyplot.plot().

import numpy as np # imports a fast numerical programming library
import scipy as sp #imports stats functions, amongst other things
import matplotlib as mpl # this actually imports matplotlib
import matplotlib.cm as cm #allows us easy access to colormaps
import matplotlib.pyplot as plt #sets up plotting under plt
import pandas as pd #lets us handle data as dataframes
#sets up pandas table display
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns #sets up styles and gives us more plotting options


# In[7]:


df=pd.read_csv("all.csv", header=None,
               names=["rating", 'review_count', 'isbn', 'booktype','author_url', 'year', 'genre_urls', 'dir','rating_count', 'name'],
)
df.head()


# In[8]:


df.dtypes


# In[9]:


df.shape


# In[10]:


df.shape[0], df.shape[1]


# In[11]:


df.columns


# In[12]:


type(df.rating), type(df)


# In[13]:


df.rating < 3


# In[14]:


np.sum(df.rating < 3)


# In[16]:


print(1*True, 1*False)


# In[17]:


np.sum(df.rating < 3)/df.shape[0]


# In[18]:


np.mean(df.rating < 3.0)


# In[19]:


(df.rating < 3).mean()


# In[20]:


df.query("rating > 4.5")


# In[21]:


df[df.year < 0]


# In[22]:


df[(df.year < 0) & (df.rating > 4)]#there were none greater than 4.5!


# In[23]:


df.dtypes


# In[24]:


df['rating_count']=df.rating_count.astype(int)
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)


# In[25]:


df[df.year.isnull()]


# In[26]:


df = df[df.year.notnull()]
df.shape


# In[27]:


df['rating_count']=df.rating_count.astype(int)
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)


# In[28]:


df.dtypes


# In[29]:


df.rating.hist();


# In[52]:


sns.set_context("notebook")
meanrat=df.rating.mean()
#you can get means and medians in different ways
print(meanrat, np.mean(df.rating), df.rating.median())
with sns.axes_style("whitegrid"):
    df.rating.hist(bins=30, alpha=0.4);
    plt.axvline(meanrat, 0, 0.75, color='r', label='Mean')
    plt.xlabel("average rating of book")
    plt.ylabel("Counts")
    plt.title("Ratings Histogram")
    plt.legend()
    #sns.despine()


# In[31]:


sns.set_context("notebook")
meanrat=df.rating.mean()
#you can get means and medians in different ways
print(meanrat, np.mean(df.rating), df.rating.median())
with sns.axes_style("whitegrid"):
    df.rating.hist(bins=30, alpha=0.4);
    plt.axvline(meanrat, 0, 0.75, color='r', label='Mean')
    plt.xlabel("average rating of book")
    plt.ylabel("Counts")
    plt.title("Ratings Histogram")
    plt.legend()
    #sns.despine()


# In[32]:


df.review_count.hist(bins=np.arange(0, 40000, 400))


# In[33]:


df.review_count.hist(bins=100)
plt.xscale("log");


# In[34]:


plt.scatter(df.year, df.rating, lw=0, alpha=.08)
plt.xlim([1900,2010])
plt.xlabel("Year")
plt.ylabel("Rating")


# In[35]:


alist=[1,2,3,4,5]


# In[36]:


asquaredlist=[i*i for i in alist]
asquaredlist


# In[37]:


plt.scatter(alist, asquaredlist);


# In[51]:


print(type(alist))


# In[50]:


print(type(alist))


# In[40]:


print(alist)


# In[41]:


plt.hist(df.rating_count.values, bins=100, alpha=0.5);


# In[49]:


print(type(df.rating_count), type(df.rating_count.values))


# In[43]:


alist + alist


# In[44]:


np.array(alist)


# In[45]:


np.array(alist)+np.array(alist)


# In[46]:


np.array(alist)**2


# In[47]:


newlist=[]
for item in alist:
    newlist.append(item+item)
newlist


# In[48]:


a=np.array([1,2,3,4,5])
print(type(a))

b=np.array([1,2,3,4,5])

print(a*b)


# In[53]:


a+1


# In[ ]:




