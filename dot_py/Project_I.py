#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from pathlib import Path
import csv
import sys


#Open txt file and store as variable. 
starting_value_str = open("../The_Hodlers/starting_value.txt",'r')
#Read starting value and convert to float. 
starting_value = float(starting_value_str.read())

#Read in the CSV file called "TRX_USD.csv" using the path module. 
trx_path = Path('./csv_data/csv_files_crypto/TRX_USD.csv')

#Read trx csv into pandas dataframe, indexing date.
trx_df = pd.read_csv(
        trx_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)

#Filter out 'close' price into a sliced dataframe. 
trx_sliced = trx_df.iloc[:,[3]]


# In[16]:


#Rename 'close' price to 'TRX/USD' in a new dataframe.
trx_new = trx_sliced.rename(columns={"Close":'TRX/USD'})


# In[17]:


#Read in the CSV file called "BTC_USD.csv" using the path module.
btc_path = Path('./csv_data/csv_files_crypto/BTC_USD.csv')

#Read btc csv into pandas dataframe, indexing date.
btc_df = pd.read_csv(
        btc_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)


# In[18]:


#Verify 'close' data-type as "float.


# In[19]:


#Filter out 'close' price into sliced dataframe. 
btc_sliced = btc_df.iloc[:,[3]]


# In[20]:


#Rename 'close' price to 'BTC/USD' in a new dataframe.
btc_new = btc_sliced.rename(columns={"Close":"BTC/USD"})

#Display the top 5 results.



# In[21]:


#Read in the CSV file called "ETH_USD.csv" using the path module. 
eth_path = Path('./csv_data/csv_files_crypto/ETH_USD.csv')

#Read eth csv into pandas dataframe, indexing date.
eth_df = pd.read_csv(
        eth_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)


# In[22]:





# In[23]:


#Filter out 'close' price into sliced dataframe. 
eth_sliced=eth_df.iloc[:,[3]]


# In[24]:


#Rename 'close' price to 'ETH/USD' in a new dataframe.
eth_new = eth_sliced.rename(columns={"Close":"ETH/USD"})




# In[25]:


#Read in the CSV file called "XLM_USD.csv" using the path module. 
xlm_path = Path('./csv_data/csv_files_crypto/XLM_USD.csv')

#Read xlm csv into pandas dataframe, indexing date.
xlm_df = pd.read_csv(
        xlm_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)


# In[26]:





# In[27]:


#Filter out 'close' price into sliced dataframe. 
xlm_sliced = xlm_df.iloc[:,[3]]


# In[28]:


#Rename 'close' price to 'XLM/USD' in a new dataframe. 
xlm_new = xlm_sliced.rename(columns={"Close":"XLM/USD"})




# In[29]:


#Read in the CSV file called "XMR_USD.csv" using the path module. 
xmr_path = Path('./csv_data/csv_files_crypto/XMR_USD.csv')

#Read xmr csv into pandas dataframe, indexing date.
xmr_df = pd.read_csv(
        xmr_path, index_col='Date', infer_datetime_format=True, parse_dates=True
)


# In[30]:




# In[31]:


#Filter out 'close' price into sliced dataframe. 
xmr_sliced = xmr_df.iloc[:,[3]]


# In[32]:


#Rename 'close' price to 'XMR/USD' in a new dataframe.
xmr_new = xmr_sliced.rename(columns={"Close":"XMR/USD"})



# In[33]:


#Use concatenate function to group btc_new, eth_new, trx_new, xlm_new, xmr_new dataframes into a single dataframe called 'crypto.'
crypto = pd.concat([btc_new, eth_new, trx_new, xlm_new, xmr_new], axis=1)



# In[34]:


crypto_daily_returns = crypto.pct_change()



# In[ ]:





# In[ ]:


#Calculate daily returns for xlm in a new dataframe. 
xlm_daily_returns = xlm_new.pct_change()



# In[ ]:


#Add an empty portfolio column to XLM Daily Returns. 
xlm_daily_returns['Portfolio'] = pd.NaT



# In[ ]:


#Calculate the portfolio value over time. 
xlm_daily_returns = xlm_daily_returns.assign(Portfolio=(1+xlm_daily_returns['XLM/USD'].fillna(0)).cumprod().mul(starting_value))


# In[ ]:


#Rename columns. 
xlm = xlm_daily_returns.rename(columns={'XLM/USD':'XLM Daily Returns',"Portfolio":"XLM Port"})


# In[ ]:


#Display results. 



# In[ ]:





# In[ ]:


#Calculate daily returns for XMR in a new dataframe. 
xmr_daily_returns = xmr_new.pct_change()


# In[ ]:


#Add an empty portfolio column to XMR Daily Returns. 
xmr_daily_returns['Portfolio'] = pd.NaT



# In[ ]:


#Calculate the portfolio value over time. 
xmr_daily_returns = xmr_daily_returns.assign(Portfolio=(1+xmr_daily_returns['XMR/USD'].fillna(0)).cumprod().mul(starting_value))


# In[ ]:


#Rename columns. 
xmr = xmr_daily_returns.rename(columns={'XMR/USD':'XMR Daily Returns',"Portfolio":"XMR Port"})


# In[ ]:




# In[ ]:





# In[ ]:


#Calculate daily returns for ETH in a new dataframe. 
eth_daily_returns = eth_new.pct_change()


# In[37]:


#Add an empty portfolio column to ETH Daily Returns. 
eth_daily_returns['Portfolio'] = pd.NaT



# In[38]:


#Calculate the portfolio value over time. 
eth_daily_returns = eth_daily_returns.assign(Portfolio=(1+eth_daily_returns['ETH/USD'].fillna(0)).cumprod().mul(starting_value))


# In[39]:


#Rename columns. 
eth = eth_daily_returns.rename(columns={'ETH/USD':'ETH Daily Returns',"Portfolio":"ETH Port"})


# In[40]:





# In[ ]:





# In[41]:


#Calculate daily returns for BTC in a new dataframe. 
btc_daily_returns = btc_new.pct_change()


# In[42]:


#Add an empty portfolio column to BTC Daily Returns. 
btc_daily_returns['Portfolio'] = pd.NaT



# In[43]:


#Calculate the portfolio value over time. 
btc_daily_returns = btc_daily_returns.assign(Portfolio=(1+btc_daily_returns['BTC/USD'].fillna(0)).cumprod().mul(starting_value))


# In[44]:


#Rename columns. 
btc = btc_daily_returns.rename(columns={'BTC/USD':'BTC Daily Returns',"Portfolio":"BTC Port"})


# In[45]:



# In[ ]:





# In[46]:


#Calculate daily returns for TRX in a new dataframe. 
trx_daily_returns = trx_new.pct_change()


# In[47]:


#Add an empty portfolio column to TRX Daily Returns. 
trx_daily_returns['Portfolio'] = pd.NaT




# In[48]:


#Calculate the portfolio value over time. 
trx_daily_returns = trx_daily_returns.assign(Portfolio=(1+trx_daily_returns['TRX/USD'].fillna(0)).cumprod().mul(starting_value))


# In[49]:


#Rename columns. 
trx = trx_daily_returns.rename(columns={'TRX/USD':'TRX Daily Returns',"Portfolio":"TRX Port"})


# In[50]:



# In[ ]:





# In[51]:


#Use concatenate function to group the daily_returns and port values into one dataframe. 
crypto_new = pd.concat([btc, eth, trx, xmr, xlm],axis=1)



# In[53]:


#Drop 'Daily Returns' column. 
crypto_sliced = crypto_new.iloc[:,[1,3,5,7,9]]



#Create a dataframe to filter out daily returns % change.
crypto_sliced_vol = crypto_new.iloc[:,[0,2,4,6,8]]






