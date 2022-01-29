#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Import the required libraries and dependencies.
import pandas as pd
from pathlib import Path
# Import the NumPy library
import numpy as np
import csv
import sys
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go

starting_value_str = open("../The_Hodlers/starting_value.txt",'r')
starting_value = float(starting_value_str.read())


# Read in the CSV file called "AMC_.csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
AMC_df = pd.read_csv(
    Path('./csv_data/csv_files_stocks/AMC_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[25]:


# Preview AMC_df file



# In[26]:


# For the AMC_df, replace or drop all NaNs or missing values in the DataFrame
AMC_df.dropna()


# In[27]:


# Convert the Close data type to a float
AMC_df.loc[:,"Close"] = AMC_df.loc[:,"Close"].astype("float")



# In[28]:


#Review the data for duplicated values, and drop them if necessary.
AMC_df.drop_duplicates()


# In[29]:


# Use loc or iloc to select `Date (the index)` and `Close` from bitstamp DataFrame
AMC_sliced = AMC_df.iloc[:,[3]]
# Review the first 5 rows of DataFrame


# In[31]:


# Rename colummn Close to AMC 
AMC_new = AMC_sliced.rename(columns={"Close":"AMC"})
# Display the result



# In[32]:


# Read in the CSV file called "GME_.csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
GME_df = pd.read_csv(
    Path('./csv_data/csv_files_stocks/GME_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[33]:





# In[34]:


GME_df.dropna()


# In[35]:


# Convert the Close data type to a float
GME_df.loc[:,"Close"] = GME_df.loc[:,"Close"].astype("float")


# In[36]:


#Review the data for duplicated values, and drop them if necessary.
GME_df.drop_duplicates()


# In[37]:


# Use loc or iloc to select `Date (the index)` and `Close` from GME DataFrame
GME_sliced = GME_df.iloc[:,[3]]
# Review the first 5 rows of DataFrame




# In[39]:


# Rename colummn Close to AMC 
GME_new = GME_sliced.rename(columns={"Close":"GME"})



# In[40]:


# Using concat function to merge AMC and GME into one DataFrame
result = pd.concat([AMC_new,GME_new], axis = 1)



# In[41]:


# Read in the CSV file called "MSTR_csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
MSTR_df = pd.read_csv(
    Path('./csv_data/csv_files_stocks/MSTR_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[42]:




# In[43]:


# Convert the Close data type to a float
MSTR_df.loc[:,"Close"] = MSTR_df.loc[:,"Close"].astype("float")


# In[44]:


# Use loc or iloc to select `Date (the index)` and `Close` from bitstamp DataFrame
MSTR_sliced = MSTR_df.iloc[:,[3]]


# In[45]:


# Rename colummn Close to MSTR
MSTR_new = MSTR_sliced.rename(columns={"Close":"MSTR"})



# In[46]:


# Using concat function to merge AMC,GME, MSTR into one DataFrame
result = pd.concat([AMC_new,GME_new, MSTR_new], axis = 1)


# In[47]:


# Read in the CSV file called "SPY_csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
SPY_df = pd.read_csv(
    Path('./csv_data/csv_files_stocks/SPY_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)


# In[48]:





# In[49]:


# Convert the Close data type to a float
SPY_df.loc[:,"Close"] = SPY_df.loc[:,"Close"].astype("float")


# In[50]:


# Use loc or iloc to select `Date (the index)` and `Close` from DataFrame
SPY_sliced = SPY_df.iloc[:,[3]]



# In[51]:


# Rename colummn Close to SPY
SPY_new = SPY_sliced.rename(columns={"Close":"SPY"})



# In[52]:


# Using concat function to merge AMC,GME, MSTR, SPY into one DataFrame
result = pd.concat([AMC_new,GME_new, MSTR_new, SPY_new], axis = 1, join = 'inner')


# In[53]:


# Read in the CSV file called "TSLA_csv" using the Path module. 
# The CSV file is located in the Stock_Prices folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters
TSLA_df = pd.read_csv(
    Path('./csv_data/csv_files_stocks/TSLA_csv_file.csv'), 
    index_col="Date", 
    parse_dates=True, 
    infer_datetime_format=True)



# In[55]:


# Convert the Close data type to a float
TSLA_df.loc[:,"Close"] = TSLA_df.loc[:,"Close"].astype("float")


# In[56]:


# Use loc or iloc to select `Date (the index)` and `Close` from DataFrame
TSLA_sliced = TSLA_df.iloc[:,[3]]



# In[57]:


# Rename colummn Close to TSLA
TSLA_new = TSLA_sliced.rename(columns={"Close":"TSLA"})


# In[58]:


# Using concat function to merge AMC,GME, MSTR, SPY and TSLA into one DataFrame
result_df = pd.concat([AMC_new,GME_new, MSTR_new, SPY_new,TSLA_new], axis = 1, join = 'inner')



# In[59]:




# In[60]:


# Calculate the daily returns each stocks in result_df DataFrame
stocks_daily_return = result_df.pct_change().dropna()




# In[71]:


# Create a daily return for AMC in a new dataframe
AMC_daily_returns = AMC_new.pct_change()
# Review AMC daily returns




# In[72]:


# Add an empty "Portfolio" column for AMC_daily_returns in order
# to keep tracking the AMC cumulative return with types as NaT(represent missing value) DataFrame
AMC_daily_returns['Portfolio'] = pd.NaT



# In[73]:

starting_value = 1200
# Calculate the AMC cumulative value over time 
AMC_daily_returns = AMC_daily_returns.assign(Portfolio=(1+AMC_daily_returns['AMC'].fillna(0)).cumprod().mul(starting_value))


# In[74]:




# In[75]:


#Rename columns. 
AMC = AMC_daily_returns.rename(columns={'AMC':'AMC Daily Returns',"Portfolio":"AMC Port"})
# Review AMC Data Frame

# In[76]:


# Create a daily return for GME in a new dataframe
GME_daily_returns = GME_new.pct_change()


# In[77]:


# Add an empty "Portfolio" column for GME_daily_returns in order
# to keep tracking the AMC cumulative return with types as NaT(represent missing value) DataFrame
GME_daily_returns['Portfolio'] = pd.NaT


# In[78]:


# Calculate the GME cumulative value over time 
GME_daily_returns = GME_daily_returns.assign(Portfolio=(1+GME_daily_returns['GME'].fillna(0)).cumprod().mul(starting_value))


# In[79]:


#Rename columns. 
GME = GME_daily_returns.rename(columns={'GME':'GME Daily Returns',"Portfolio":"GME Port"})

# In[80]:


# Create a daily return for MSTR in a new dataframe
MSTR_daily_returns = MSTR_new.pct_change()
# In[81]:


# Add an empty "Portfolio" column for MSTR_daily_returns in order
# to keep tracking the MSTR cumulative return with types as NaT(represent missing value) DataFrame
MSTR_daily_returns['Portfolio'] = pd.NaT

# In[82]:


# Calculate the MSTR cumulative value over time 
MSTR_daily_returns = MSTR_daily_returns.assign(Portfolio=(1+MSTR_daily_returns['MSTR'].fillna(0)).cumprod().mul(starting_value))
# Review GME_daily_returns

# In[83]:


#Rename columns. 
MSTR = MSTR_daily_returns.rename(columns={'MSTR':'MSTR Daily Returns',"Portfolio":"MSTR Port"})
# Review MSTR Data Frame



# In[84]:


# Create a daily return for SPY in a new dataframe
SPY_daily_returns = SPY_new.pct_change()
# Review AMC daily returns


# In[85]:


# Add an empty "Portfolio" column for MSTR_daily_returns in order
# to keep tracking the MSTR cumulative return with types as NaT(represent missing value) DataFrame
SPY_daily_returns['Portfolio'] = pd.NaT



# In[86]:


# Calculate the SPY cumulative value over time 
SPY_daily_returns = SPY_daily_returns.assign(Portfolio=(1+SPY_daily_returns['SPY'].fillna(0)).cumprod().mul(starting_value))



# In[87]:


#Rename columns. 
SPY = SPY_daily_returns.rename(columns={'SPY':'SPY Daily Returns',"Portfolio":"SPY Port"})



# In[88]:


# Create a daily return for TSLA in a new dataframe
TSLA_daily_returns = TSLA_new.pct_change()



# In[89]:


# Add an empty "Portfolio" column for TSLA_daily_returns in order
# to keep tracking the TSLA cumulative return with types as NaT(represent missing value) DataFrame
TSLA_daily_returns['Portfolio'] = pd.NaT

# In[90]:
# Calculate the TSLA cumulative value over time 
TSLA_daily_returns = TSLA_daily_returns.assign(Portfolio=(1+TSLA_daily_returns['TSLA'].fillna(0)).cumprod().mul(starting_value))

# In[91]:


#Rename columns. 
TSLA = TSLA_daily_returns.rename(columns={'TSLA':'TSLA Daily Returns',"Portfolio":"TSLA Port"})



# In[94]:


#Use concatenate function to group the daily_returns and port values into one dataframe. 
stocks_new = pd.concat([AMC, GME, MSTR, SPY, TSLA],axis=1, join ='inner')


# In[96]:


#Drop 'Daily Returns' column. 
stocks_sliced = stocks_new.iloc[:,[1,3,5,7,9]]


#Create a dataframe to filter out daily returns % change.
stocks_sliced_vol = stocks_new.iloc[:, [0,2,4,6,8]]

