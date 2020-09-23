#!/usr/bin/env python
# coding: utf-8

# Installation Packages and Libraries

# In[19]:


#Installation Packages
"""!pip install dash-renderer
!pip install dash
!pip install dash-html-components
!pip install dash-core-components
!pip install plotly"""


# In[20]:


#loading dash libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import numpy as np


# Loading Data and Basic Exploration

# In[21]:


df=pd.read_csv("SynesisIT (2).csv", sep=';')
df.head()


# In[22]:


df['DateTime']=df['Date']+' '+df['Time']


# In[23]:


df.tail()


# In[24]:


df1=df.loc[df.Date==max(df.Date)]


# In[25]:


df1.head()


# In[26]:


df1.columns


# Plots and Design

# In[27]:


app=dash.Dash()
server=app.server
app.layout= html.Div([
    html.H1('Energy Meter Dashboard'),
    
    dcc.Graph(
        id='line_current',
        figure={            
                'data':[ 
                {'x': df1.DateTime, 'y': df1.phase_1_current,'name':'phase_1_current'},
                {'x': df1.DateTime, 'y': df1.phase_2_current,'name':'phase_2_current', 'marker' : { "color" : 'rgb(255,0,0)'}},
                {'x': df1.DateTime, 'y': df1.phase_3_current,'name':'phase_3_current', 'marker' : { "color" : 'rgb(255,255,0)'}}
                        ],
                'layout':go.Layout(title='Phase Current')           
                }
            ),
    
    dcc.Graph(
        id='line_pf',
        figure={            
                'data':[ 
                {'x': df1.DateTime, 'y': df1.phase_1_power_factor,'name':'phase_1_power_factor'},
                {'x': df1.DateTime, 'y': df1.phase_2_power_factor,'name':'phase_2_power_factor', 'marker' : { "color" : 'rgb(255,0,0)'}},
                {'x': df1.DateTime, 'y': df1.phase_3_power_factor,'name':'phase_3_power_factor', 'marker' : { "color" : 'rgb(255,255,0)'}}
                        ],
                'layout':go.Layout(title='Phase PF')          
                }
            ) 
    
])


# Server integration for running real time

# In[28]:




# In[29]:




