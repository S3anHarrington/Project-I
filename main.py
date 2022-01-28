import sys
import csv
import pandas as pd 
from pathlib import Path

import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go

#Import Portfolio df of each asset category.
from dot_py.cleaned_df import agriculture_daily_returns_sliced 
from dot_py.Project_I import crypto_sliced
from dot_py.Stimulus_Check_Profit_Analyzer import resources_sliced
from dot_py.Stocks_Price import stocks_sliced 

#Import Daily Returns(%) df of each asset category.
from dot_py.Project_I import crypto_sliced_vol
from dot_py.cleaned_df import agriculture_daily_returns_sliced_vol
from dot_py.Stimulus_Check_Profit_Analyzer import resources_sliced_vol
from dot_py.Stocks_Price import stocks_sliced_vol

#Concatenate portfolio dataframes into one. 
final_port = pd.concat([crypto_sliced, agriculture_daily_returns_sliced, resources_sliced, stocks_sliced], axis=1).dropna() #otherwise there are gaps in the lines due to 24/7 crypto tradeability. 

#Concatenate daily returns % dataframes into one. 
final_port_vol = pd.concat([agriculture_daily_returns_sliced_vol, crypto_sliced_vol, resources_sliced_vol, stocks_sliced_vol], axis=1).dropna()  #otherwise there are gaps in the lines due to 24/7 crypto tradeability. 

#Build a figure for the portfolio dataframe.
fig = px.line(final_port, x=final_port.index, y = final_port.columns)
#Map lines/series to groups
maps = {'Agriculture': ['Wheat Port', 'Corn Port','Hogs Port', 'FD Cattle Port', 'GF Cattle Port'],
        'Natural Resources': ['Gold Port', 'Silver Port','Crude Oil Port','Lumber Port','Gasoline Port'],
        'Stocks': ['MSTR Port', "GME Port", "TSLA Port", "SPY Port", "AMC Port"],
        'Crypto':['TRX Port', 'XMR Port', "XLM Port", "BTC Port", "ETH Port"],}

#Create group and trace visibilites
group = []
vis = []
visList = []
for m in maps.keys():
    for col in final_port.columns:
        if col in maps[m]:
            vis.append(True)
        else:
            vis.append(False)
    group.append(m)
    visList.append(vis)
    vis = []
    
#Create buttons for each group
buttons = []
for i, g in enumerate(group):
    button =  dict(label=g,
                   method = 'restyle',
                    args = ['visible',visList[i]])
    buttons.append(button)

buttons = [{'label': 'all',
                 'method': 'restyle',
                 'args': ['visible', [True, True, True, True, True, True]]}] + buttons

                     

# update layout with buttons                       
fig.update_layout(
    updatemenus=[
        dict(
        type="dropdown",
        direction="down",
        buttons = buttons)
    ],
)
# buttons
fig.show()



#Create graph for Daily Returns (%)
#Create a plot for daily returns to demonstrate volatility. 
#Build a figure for all series
fig_dr = px.line(final_port_vol, x=final_port_vol.index, y = final_port_vol.columns)
#Map lines/series to groups
maps = {'Crypto': ['BTC Daily Returns', 'ETH Daily Returns', 'TRX Daily Returns', 'XMR Daily Returns', 'XLM Daily Returns'],
        'Natural Resources': ['Gold Daily Returns', 'Silver Daily Returns', 'Crude Oil Daily Returns', 'Lumber Daily Returns', 'Gasoline Daily Returns'],
        'Stocks': ['MSTR Daily Returns','AMC Daily Returns','GME Daily Returns','SPY Daily Returns','TSLA Daily Returns'],
        'Agriculture':['Wheat Daily Returns', 'Corn Daily Returns', "FD Cattle Daily Returns", "Hogs Daily Returns", 'GF Cattle']}

#Create group and trace visibilites
group = []
vis = []
visList = []
for m in maps.keys():
    for col in final_port_vol.columns:
        if col in maps[m]:
            vis.append(True)
        else:
            vis.append(False)
    group.append(m)
    visList.append(vis)
    vis = []
    
#Create buttons for each group
buttons = []
for i, g in enumerate(group):
    button =  dict(label=g,
                   method = 'restyle',
                    args = ['visible',visList[i]])
    buttons.append(button)

buttons = [{'label': 'all',
                 'method': 'restyle',
                 'args': ['visible', [True, True, True, True, True, True]]}] + buttons

                     

# update layout with buttons                       
fig_dr.update_layout(
    updatemenus=[
        dict(
        type="dropdown",
        direction="down",
        buttons = buttons)
    ],
)
# buttons
fig_dr.show()