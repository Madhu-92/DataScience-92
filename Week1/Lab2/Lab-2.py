#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")


# In[4]:


req


# In[5]:


type(req)


# In[6]:


dir(req)


# In[7]:


page = req.text
page


# In[11]:


from bs4 import BeautifulSoup


# In[12]:


soup = BeautifulSoup(page, 'html.parser')


# In[13]:


soup


# In[14]:


type(soup)


# In[15]:


type(page)


# In[16]:


print(soup.prettify())


# In[17]:


soup.title


# In[18]:


'title' in dir(soup)


# In[19]:


soup.p


# In[20]:


len(soup.find_all('p'))


# In[21]:


soup.find_all('p')


# In[22]:


soup.table['class']


# In[23]:


soup.find_all('table')


# In[24]:


[t["class"] for t in soup.find_all("table") if t.get("class")]


# In[25]:


my_list = []

for li in soup.find_all('table'):
  if li.get('class'):
    my_list.append(li['class'])

my_list


# In[26]:


rows = [row for row in soup.find_all("table", "wikitable")[2].find_all("tr")]
rows


# In[27]:


table_html = str(soup.find_all('table', 'wikitable')[2])
table_html


# In[28]:


from IPython.core.display import HTML
HTML(table_html)


# In[29]:


rem_nl = lambda s : s.replace("\n", "")
rem_nl


# In[30]:


def power(x, y):
  return x **y
power(2, 3)


# In[31]:


def print_greetings():
  return "Hello World"

print_greetings()


# In[32]:


def get_multiple(x, y=1):
  return x * y

print("with x and y:", get_multiple(10, 2))
print("with x only:", get_multiple(10))


# In[33]:


def print_special_greeting(name, leaving=False, condition="nice"):
  print("Hello", name)
  print("How are you doing on this", condition, "day?")
  if leaving:
    print("Please come back")


# In[34]:


print_special_greeting("John")


# In[35]:


print_special_greeting("Sahith", True)


# In[36]:


print_special_greeting("Sathwik", True, "Hot")


# In[37]:


def print_siblings(name, *siblings):
  print(name, "has the following siblings")
  for sibling in siblings:
    print(sibling)
    
print_siblings("Sahith", "Sathwik")


# In[38]:


def print_brothers_and_sisters(name, **siblings):
  print(name, "has the following siblings")
  for sibling in siblings:
    print(sibling, ":", siblings[sibling])
  print()
  
print_brothers_and_sisters("Sahith", Sathwik="brother")


# In[39]:


columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
columns


# In[40]:


indexes = [row.find("th").get_text() for row in rows[1:]]
indexes


# In[41]:


to_num = lambda s : s[-1] == "%" and int(s[:-1]) or None


# In[42]:


HTML(table_html)


# In[43]:


rows


# In[44]:


values = [to_num(rem_nl(value.get_text())) for row in rows[1:] for value in row.find_all("td")]
values


# In[45]:


# stacked_values = zip(*[values[i::3] for i in range(len(columns))])
# list(stacked_values)

stacked_values = zip(*[values[i::3] for i in range(len(columns))])
list(stacked_values)


# In[46]:


def print_args(arg1, arg2, arg3):
  print(arg1, arg2, arg3)
  
print_args(1, 2, 3)
print_args([1, 10], [2, 20], [3, 30])


# In[47]:


parameters = [100, 200, 300]

p1 = parameters[0]
p2 = parameters[1]
p3 = parameters[2]

print_args(p1, p2, p3)


# In[48]:


p4, p5, p6 = parameters
print_args(p4, p5, p6)


# In[49]:


print_args(*parameters)


# In[50]:


my_dict = {ind : value for ind, value in zip(indexes, values)}
my_dict


# In[51]:


import pandas as pd


# In[52]:


# d = {columns[0]:indexes,columns[1]:values}
# df = pd.DataFrame(d)
# df

# d = list(zip(indexes, values))
# df = pd.DataFrame(d, columns=columns)
# df

stacked_values = zip(*[values[i::3] for i in range(len(columns))])
df = pd.DataFrame(stacked_values, columns=columns, index=indexes)
df


# In[53]:


df.dtypes


# In[54]:


#df.dropna()
#df_clean = df.fillna(0).astype(int)

df.describe()


# In[55]:


import numpy as np


# In[56]:


df.values


# In[57]:


type(df.values)


# In[58]:


stacked_values = zip(*[values[i::3] for i in range(len(columns))])
columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
data_dicts = [{col : val for col, val in zip(columns, col_values)} for col_values in stacked_values]
data_dicts


# In[59]:


pd.DataFrame(data_dicts, index=indexes)


# In[60]:


df.dropna()


# In[61]:


df.dropna(axis=1)


# In[62]:


df_new = df.fillna(0).astype(int)
df_new


# In[63]:


df_new.dtypes


# In[64]:


df_new.describe()


# In[65]:


type(df_new.values)


# In[66]:


np.mean(df_new.values)


# In[67]:


np.mean(df_new.Undergrad)


# In[68]:


np.std(df_new)


# In[69]:


df_new['Undergrad']


# In[70]:


df['Graduate']


# In[71]:


df_new.Undergrad


# In[72]:


df_new.iloc[0]


# In[73]:


df_new.ix[3, "Graduate"]


# In[74]:


sequence_table = df_new.stack().reset_index()
sequence_table.columns = ["race", "source", "percentage"]
sequence_table


# In[75]:


grouped_data = sequence_table.groupby("race")
grouped_data.groups


# In[76]:


type(grouped_data)


# In[77]:


mean_of_table = grouped_data.mean()
mean_of_table


# In[78]:


type(mean_of_table)


# In[79]:


for name, group in sequence_table.groupby("source", sort=True):
  print(name)
  print(group)


# In[80]:


import matplotlib


# In[81]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[82]:


mean_of_table.plot(kind="bar")


# In[ ]:




