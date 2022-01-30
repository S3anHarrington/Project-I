#!/usr/bin/env python
# coding: utf-8

# # Stimulous Check Profit Analyzer

# In[2]:


# Import the required libraries and dependencies.
import pandas as pd
from pathlib import Path
import csv
import sys


#Open txt file. 
starting_value_str = open("../The_Hodlers/starting_value.txt",'r')
#Read starting value and convert to float. 
starting_value = float(starting_value_str.read())


# Read in the CSV file called "Resources.csv" using the Path module.
# The CSV file is located int the Stimulous_Check_Profit_Analyzer folder.
# Set the index to the column "Date".
# Set the parse_date and infer_datetime_format parameters.
gold_df = pd.read_csv(
    Path('./csv_data/csv_files_resources/gold.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)




# In[4]:


# Filter out 'Gold Close' price into a sliced dataframe. 
gold_sliced = gold_df.iloc[:,[0]]

#Rename 'close' price to 'Gold' in a new dataframe.
gold_new = gold_sliced.rename(columns={"Price":'Gold'})



# In[12]:


silver_df = pd.read_csv(
    Path('./csv_data/csv_files_resources/silver.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)



# In[13]:


# Filter out 'Silver Close' price into a sliced dataframe. 
silver_sliced = silver_df.iloc[:,[0]]

#Rename 'close' price to 'Silver' in a new dataframe.
silver_new = silver_sliced.rename(columns={"Price":'Silver'})




# In[14]:


crude_oil_df = pd.read_csv(
    Path('./csv_data/csv_files_resources/crude_oil.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)



# In[15]:


# Filter out 'Crude Oil Close' price into a sliced dataframe. 
crude_oil_sliced = crude_oil_df.iloc[:,[0]]

#Rename 'close' price to 'Crude Oil' in a new dataframe.
crude_oil_new = crude_oil_sliced.rename(columns={"Price":'Crude Oil'})




# In[16]:


lumber_df = pd.read_csv(
    Path('./csv_data/csv_files_resources/lumber.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)



# In[17]:


# Filter out 'Lumber Close' price into a sliced dataframe. 
lumber_sliced = lumber_df.iloc[:,[0]]

#Rename 'close' price to 'Lumber' in a new dataframe.
lumber_new = lumber_sliced.rename(columns={"Price":'Lumber'})




# In[18]:


gasoline_df = pd.read_csv(
    Path('./csv_data/csv_files_resources/gasoline.csv'),
    index_col = 'Date',
    parse_dates = True,
    infer_datetime_format = True)



# In[19]:


# Filter out 'Gasoline Close' price into a sliced dataframe. 
gasoline_sliced = gasoline_df.iloc[:,[0]]

#Rename 'close' price to 'Lumber' in a new dataframe.
gasoline_new = gasoline_sliced.rename(columns={"Price":'Gasoline'})



# In[104]:


# Use concatenate function to group btc_new, eth_new, trx_new, xlm_new, xmr_new dataframes into a single dataframe called 'resources'.
resources = pd.concat([gold_new, silver_new, crude_oil_new, lumber_new, gasoline_new], axis=1)



# In[105]:


resources_daily_returns = resources.pct_change()



# In[106]:





# In[107]:




# In[112]:


#Calculate daily returns for Gold in a new dataframe. 
gold_daily_returns = gold_new.pct_change()




# In[113]:


#Add an empty portfolio column to Gold Daily Returns. 
gold_daily_returns['Portfolio'] = pd.NaT




# In[125]:


#Calculate the portfolio value over time. 
gold_daily_returns = gold_daily_returns.assign(Portfolio=(1+gold_daily_returns['Gold'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
gold = gold_daily_returns.rename(columns={'Gold':'Gold Daily Returns', "Portfolio":"Gold Port"})




# In[114]:


#Calculate daily returns for Silver in a new dataframe. 
silver_daily_returns = silver_new.pct_change()



# In[115]:


#Add an empty portfolio column to Silver Daily Returns. 
silver_daily_returns['Portfolio'] = pd.NaT




# In[126]:


#Calculate the portfolio value over time. 
silver_daily_returns = silver_daily_returns.assign(Portfolio=(1+silver_daily_returns['Silver'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
silver = silver_daily_returns.rename(columns={'Silver':'Silver Daily Returns',"Portfolio":"Silver Port"})




# In[119]:


#Calculate daily returns for Crude Oil in a new dataframe. 
crude_oil_daily_returns = crude_oil_new.pct_change()




# In[120]:


#Add an empty portfolio column to Crude Oil Daily Returns. 
crude_oil_daily_returns['Portfolio'] = pd.NaT



# In[128]:


#Calculate the portfolio value over time. 
crude_oil_daily_returns = crude_oil_daily_returns.assign(Portfolio=(1+crude_oil_daily_returns['Crude Oil'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
crude_oil = crude_oil_daily_returns.rename(columns={'Crude Oil':'Crude Oil Daily Returns', "Portfolio": "Crude Oil Port"})




# In[121]:


#Calculate daily returns for Lumber in a new dataframe. 
lumber_daily_returns = lumber_new.pct_change()


#Add an empty portfolio column to Lumber Daily Returns. 
lumber_daily_returns['Portfolio'] = pd.NaT





#Calculate the portfolio value over time. 
lumber_daily_returns = lumber_daily_returns.assign(Portfolio=(1+lumber_daily_returns['Lumber'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
lumber = lumber_daily_returns.rename(columns={'Lumber':'Lumber Daily Returns', "Portfolio": "Lumber Port"})



# In[123]:


#Calculate daily returns for Gasoline in a new dataframe. 
gasoline_daily_returns = gasoline_new.pct_change()



# In[124]:


#Add an empty portfolio column to Gasoline Daily Returns. 
gasoline_daily_returns['Portfolio'] = pd.NaT




# In[131]:


#Calculate the portfolio value over time. 
gasoline_daily_returns = gasoline_daily_returns.assign(Portfolio=(1+gasoline_daily_returns['Gasoline'].fillna(0)).cumprod().mul(starting_value))

#Rename columns. 
gasoline = gasoline_daily_returns.rename(columns={'Gasoline':'Gasoline Daily Returns', "Portfolio":"Gasoline Port"})




# In[136]:


#Use concatenate function to group the daily_returns and port values into one dataframe. 
resources_new = pd.concat([gold, silver, crude_oil, lumber, gasoline],axis=1)



#Drop 'Daily Returns' column. 
resources_sliced = resources_new.iloc[:,[1,3,5,7,9]]

#Create a dataframe to filter out daily returns % change.
resources_sliced_vol = resources_new.iloc[:, [0,2,4,6,8]]
