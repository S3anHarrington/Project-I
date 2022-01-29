#!/usr/bin/env python
# coding: utf-8

# In[3]:

import pandas as pd
from pathlib import Path
import csv
import sys

#Open txt file as a variable. 
starting_value_str = open("../The_Hodlers/starting_value.txt",'r')
#Read starting value.
starting_value = (starting_value_str.read())
#Convert to float
starting_value = float(starting_value)

# In[4]:


wheat_df = pd.read_csv(
    Path("./csv_data/csv_files_agriculture/zw_wheat.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)


wheat_df = wheat_df.drop(columns=['Volume', 'Open', 'High', 'Low'])



# In[5]:


wheat_df = wheat_df.rename(columns={'Close/Last' : 'Wheat'})



# In[77]:


# Filtering my dataframes so that dates that are unused are removed.


wheat_cleaned = wheat_df.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')



# In[78]:





# In[7]:


corn_df = pd.read_csv(
    Path("./csv_data/csv_files_agriculture/zc_corn.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)

corn_df = corn_df.drop(columns=['Volume', 'Open', 'High', 'Low'])



# In[8]:


corn_df = corn_df.rename(columns={'Close/Last' : 'Corn'})



# In[81]:



# Filtering my dataframes so that dates that are unused are removed.
corn_cleaned = corn_df.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')



# In[9]:


fd_cattle_df = pd.read_csv(
    Path("./csv_data/csv_files_agriculture/fd_cattle.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)

fd_cattle_df = fd_cattle_df.drop(columns=['Volume', 'Open', 'High', 'Low'])




# In[13]:


fd_cattle_df = fd_cattle_df.rename(columns={'Close/Last' : 'FD Cattle'})



# In[14]:


# Filtering my dataframes so that dates that are unused are removed.
fd_cattle_cleaned = fd_cattle_df.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')



# In[15]:




# In[16]:


hogs_df = pd.read_csv(
    Path("./csv_data/csv_files_agriculture/he_hogs.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)

hogs_df = hogs_df.drop(columns=['Volume', 'Open', 'High', 'Low'])



# In[87]:


hogs_df = hogs_df.rename(columns={'Close/Last' : 'Hogs'})



# In[88]:


# Filtering my dataframes so that dates that are unused are removed.
hogs_cleaned = hogs_df.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')



# In[89]:



# In[17]:


gf_cattle = pd.read_csv(
    Path("./csv_data/csv_files_agriculture/gf_cattle.csv"),
    index_col='Date',
    parse_dates=True,
    infer_datetime_format=True
)

gf_cattle = gf_cattle.drop(columns=['Volume', 'Open', 'High', 'Low'])


# In[18]:


gf_cattle = gf_cattle.rename(columns={'Close/Last' : 'GF Cattle'})



# In[19]:


# Filtering my dataframes so that dates that are unused are removed.
gf_cattle_cleaned = gf_cattle.sort_index().truncate(before = '04/15/2020', after ='12/31/2021')



# In[93]:


# Using Concat to combine all dataframes into one

agriculture_df_closing_price = pd.concat([wheat_cleaned, corn_cleaned, fd_cattle_cleaned, hogs_cleaned, gf_cattle_cleaned], axis = 1, join = "inner")



# In[94]:


agriculture_df_daily_returns = agriculture_df_closing_price.pct_change().dropna()


# In[95]:





# In[96]:


#define the stimulus starting amoung in var



# In[98]:


# Calculate daily returns for Wheat in a new dataframe

wheat_daily_returns = wheat_cleaned.pct_change()




# In[99]:


wheat_daily_returns['Portfolio'] = pd.NaT




# In[100]:


wheat_daily_returns = wheat_daily_returns.assign(Portfolio=(1+wheat_daily_returns['Wheat'].fillna(0)).cumprod().mul(starting_value))


# In[101]:


#Rename columns. 
wheat = wheat_daily_returns.rename(columns={'Wheat':'Wheat Daily Returns',"Portfolio":"Wheat Port"})


# In[102]:


wheat.head()


# In[103]:


corn_daily_returns = corn_cleaned.pct_change()



# In[104]:


corn_daily_returns['Portfolio'] = pd.NaT




# In[105]:


corn_daily_returns = corn_daily_returns.assign(Portfolio=(1+corn_daily_returns['Corn'].fillna(0)).cumprod().mul(starting_value))


# In[106]:


corn = corn_daily_returns.rename(columns={'Corn':'Corn Daily Returns',"Portfolio":"Corn Port"})


# In[107]:





# In[108]:


fd_cattle_daily_returns = fd_cattle_cleaned.pct_change()




# In[109]:


fd_cattle_daily_returns['Portfolio'] = pd.NaT




# In[110]:


fd_cattle_daily_returns = fd_cattle_daily_returns.assign(Portfolio=(1+fd_cattle_daily_returns['FD Cattle'].fillna(0)).cumprod().mul(starting_value))


# In[111]:


fd_cattle = fd_cattle_daily_returns.rename(columns={'FD Cattle':'FD Cattle Daily Returns',"Portfolio":"FD Cattle Port"})


# In[112]:





# In[113]:


hogs_daily_returns = hogs_cleaned.pct_change()




# In[114]:


hogs_daily_returns['Portfolio'] = pd.NaT



# In[115]:


hogs_daily_returns = hogs_daily_returns.assign(Portfolio=(1+hogs_daily_returns['Hogs'].fillna(0)).cumprod().mul(starting_value))


# In[116]:


hogs = hogs_daily_returns.rename(columns={'Hogs':'Hogs Daily Returns',"Portfolio":"Hogs Port"})



# In[117]:


gf_cattle_daily_returns = gf_cattle_cleaned.pct_change()




# In[118]:


gf_cattle_daily_returns['Portfolio'] = pd.NaT




# In[119]:


gf_cattle_daily_returns = gf_cattle_daily_returns.assign(Portfolio=(1+gf_cattle_daily_returns['GF Cattle'].fillna(0)).cumprod().mul(starting_value))


# In[120]:


gf_cattle = gf_cattle_daily_returns.rename(columns={'FD Cattle':'FD Cattle Daily Returns',"Portfolio":"GF Cattle Port"})


# In[122]:


agriculture_daily_returns = pd.concat([wheat, corn, fd_cattle, hogs, gf_cattle], axis=1)


# In[123]:




# In[128]:




# In[129]:


agriculture_daily_returns_sliced = agriculture_daily_returns.iloc[:, [1,3,5,7,9]]




#Create a dataframe to filter out daily returns % change.
agriculture_daily_returns_sliced_vol = agriculture_daily_returns.iloc[:, [0,2,4,6,8]]




