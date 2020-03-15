#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:50:43 2019

@author: amin
"""

import os
import re
import json
import pprint
import random
import requests
import numpy as np
import pandas as pd
import seaborn as sns
from faker import Faker

import datetime

import dash
import dash_auth
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objs as go
from dash.dependencies import Input, Output

#%%


#TODO: markdown embeddings
#TODO: tezos localchain
environment = 'local'

if environment == 'local':
    base_path = '/home/amin/RandomPython/bricksonblocks/'

if environment == 'global':
    base_path = '/home/testpost/bricksonblocks/'



#%%

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.

    """
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km


#%%

mapbox_access_token = 'pk.eyJ1IjoiY29tcGFyZXRoZW1hcmtldGNhcCIsImEiOiJjam10NXVzaHAyYjlxM3BueHJteWU2ZjZyIn0.Wt7mAXyfMki08lHIzGjWTw'

print(dcc.__version__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

app.title = 'bricksonblocks'

VALID_USERNAME_PASSWORD_PAIRS = [['helloworld', 'incorrect'],
                                 ['bobbytables', 'correcthorsebatterystaple']]

# =============================================================================
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )
# =============================================================================

index_page = html.Div([
    dcc.Link('Ownership', href='/ownership'),
    html.Br(),
    dcc.Link('Investor Dashboard', href='/investor-dashboard'),
    html.Br(),
    dcc.Link('Browse Listings', href='/browse-listings'),
    html.Br(),
    dcc.Link('Generate Contract', href='/generate-contract'),
])



capitals = pd.read_csv(base_path+'capitals.csv')


#%%
#Unwary


def txdf():


    house_price = 200000
    deposit_amount = 30000
    deposit_percent = (deposit_amount / house_price) * 100
    owned_percent = deposit_percent
        
    base_market_rental_rate = 1500
    inflated_market_rental_rate = base_market_rental_rate
    initial_monthly_rent = base_market_rental_rate * (1 - owned_percent*0.01)
    initial_rental_rate = 6.5
    maximum_monthly_payment = initial_monthly_rent * 1.5
        
        
        
        
    monthly_acquisition_amount = initial_monthly_rent * 0.5
    monthly_acquisition_percent = (monthly_acquisition_amount / house_price) * 100
    
    
    paid_this_year = 0
    paid_total = 0
    inflation = 2
    
    print('house_price:', house_price)
    print('deposit_amount:', deposit_amount)
    print('deposit_percent:', deposit_percent)
    print('owned_percent:', owned_percent)
    print('initial_monthly_rate:', initial_rental_rate)
    print('initial_monthly_rent:', initial_monthly_rent)
    print('monthly_acquisition_amount:', monthly_acquisition_amount)
    print('monthly_acquisition_percent:', monthly_acquisition_percent)
    
    
    print()
    print()
    print()
    print()
    print()
    
    
    
    
    
    this_owned_percent = deposit_percent
    this_monthly_rent = initial_monthly_rent
    this_monthly_acquisition = monthly_acquisition_amount
    
    rent_amount = []
    acquisition_amount = []
    
    
    total_rent = 0
    total_acquired = deposit_amount
    total_paid = deposit_amount
    rent_over_time = []
    acquisition_over_time = []
    
    print('month:', 0)
    print('this_owned_percent:', (deposit_amount / house_price)*100)
    print('this_monthly_rent:', 0)
    print('this_monthly_acquisition:', 0)
    #print('paid_this_year:', paid_this_year)
    print('total_paid:', deposit_amount)
    print()    


    
    columns = ['timestamp',
               'from',
               'to',
               'amount',
               'type',
               'equity_tenant',
               'equity_financier',
               'equity_crowd']
    
    df = pd.DataFrame()    

    
    initial_tx = {'timestamp': '2015-01-01',
                  'from': 'Tenant',
                  'to': 'Financier',
                  'amount': deposit_amount,
                  'type': 'equity'}
    
    initial_tx['equity_tenant'] = deposit_amount
    initial_tx['equity_financier'] = house_price - deposit_amount
    initial_tx['equity_crowd'] = 0
    
    equity_tenant = initial_tx['equity_tenant']
    equity_financier = initial_tx['equity_financier']
    equity_crowd = initial_tx['equity_crowd']
    
    
    print(initial_tx)
    
    df = df.append(initial_tx, ignore_index=True)
    df = df[columns]
    





    this_owned_percent = deposit_percent
    this_monthly_rent = initial_monthly_rent
    this_monthly_acquisition = monthly_acquisition_amount
    
    
    total_rent = 0
    total_acquired = deposit_amount
    total_paid = deposit_amount
    rent_over_time = []
    acquisition_over_time = []
    
    print('month:', 0)
    print('this_owned_percent:', (deposit_amount / house_price)*100)
    print('this_monthly_rent:', 0)
    print('this_monthly_acquisition:', 0)
    #print('paid_this_year:', paid_this_year)
    print('total_paid:', deposit_amount)
    print()    
    
    
    
    year = 2015
    
    months_elapsed = 1
    while np.round(equity_tenant, 2) < np.round(house_price, 2):
    #while i < 5:
    

        
        for month in range(1, 13):
            
            first_of_month = str(year) + '-' + str(month).rjust(2, '0') + '-' + '01'
            #print(first_of_month)

            if np.round(equity_tenant, 2) >= np.round(house_price, 2):
                break
            
            #%% ROUND EQUITY
            
            equity_tenant = np.round(equity_tenant, 2)
            equity_financier = np.round(equity_financier, 2)
            equity_crowd = np.round(equity_crowd, 2)
            
            #%% CALCULATE PAYMENTS
        
            if months_elapsed % 12 == 0:
                inflated_market_rental_rate = base_market_rental_rate * (1 + (inflation / 100))**(months_elapsed / 12)
            
        
            this_monthly_rent = inflated_market_rental_rate * ((100 - this_owned_percent)*0.01)
            #this_monthly_rent = np.round(this_monthly_rent, 2)
            
            this_monthly_acquisition = maximum_monthly_payment - (this_monthly_rent*0.5)   
            this_monthly_acquisition = np.round(this_monthly_acquisition, 2)
        
            this_monthly_rent = np.round(this_monthly_rent * 0.5, 2)
            paid_this_month = this_monthly_rent + this_monthly_acquisition
            
            this_owned_percent = this_owned_percent + ((this_monthly_acquisition/house_price) * 100)
            
            
            if equity_tenant + this_monthly_acquisition > house_price:
                this_monthly_acquisition = np.round(house_price - equity_tenant, 2)
                
            
            total_rent += this_monthly_rent
            total_acquired += this_monthly_acquisition
            total_paid += paid_this_month
            
            total_rent = np.round(total_rent, 2)
            total_acquired = np.round(total_acquired, 2)
            total_paid = np.round(total_paid, 2)
    
            
            #%% PAY RENTS
        
            
            if np.round(equity_financier, 2) > 0:

            
                this_tx = {'timestamp': first_of_month,
                           'from': 'Tenant',
                           'to': 'Financier',
                           'amount': np.round(this_monthly_rent * (equity_financier / house_price), 2),
                           'type': 'rent'}
            
                this_tx['equity_tenant'] = equity_tenant
                this_tx['equity_financier'] = equity_financier
                this_tx['equity_crowd'] = equity_crowd
                
                #print(this_tx)
                
                df = df.append(this_tx, ignore_index=True)
                df = df[columns]


            if np.round(equity_crowd, 2) > 0:

                this_tx = {'timestamp': first_of_month,
                           'from': 'Tenant',
                           'to': 'Crowd',
                           'amount': np.round(this_monthly_rent * (equity_crowd / house_price), 2),
                           'type': 'rent'}
            
                this_tx['equity_tenant'] = equity_tenant
                this_tx['equity_financier'] = equity_financier
                this_tx['equity_crowd'] = equity_crowd
                
                #print(this_tx)
                
                df = df.append(this_tx, ignore_index=True)
                df = df[columns]



            #%% TENANT ACQUISITION

            if np.round(equity_financier, 2) > 0:
                
                #TODO
                
                if np.round(equity_financier, 2) < np.round(this_monthly_acquisition, 2):

                    temp = 0

                    this_tx = {'timestamp': first_of_month,
                               'from': 'Tenant',
                               'to': 'Financier',
                               'amount': np.round(equity_financier, 2),
                               'type': 'equity'}
                    
                    temp = np.round(equity_financier, 2)
                    
                    equity_tenant += np.round(equity_financier, 2)
                    equity_financier -= np.round(equity_financier, 2)

                    this_tx['equity_tenant'] = equity_tenant
                    this_tx['equity_financier'] = equity_financier
                    this_tx['equity_crowd'] = equity_crowd
                    
                    #print(this_tx)
                    
                    df = df.append(this_tx, ignore_index=True)
                    df = df[columns]


                    
                    this_tx = {'timestamp': first_of_month,
                               'from': 'Tenant',
                               'to': 'Crowd',
                               'amount': np.round(this_monthly_acquisition - temp, 2),
                               'type': 'equity'}
                    
                    equity_tenant += np.round(this_monthly_acquisition - temp, 2)
                    equity_crowd -= np.round(this_monthly_acquisition - temp, 2)

                    this_tx['equity_tenant'] = equity_tenant
                    this_tx['equity_financier'] = equity_financier
                    this_tx['equity_crowd'] = equity_crowd
                    
                    #print(this_tx)
                    
                    df = df.append(this_tx, ignore_index=True)
                    df = df[columns]

                
                else:

                    this_tx = {'timestamp': first_of_month,
                               'from': 'Tenant',
                               'to': 'Financier',
                               'amount': np.round(this_monthly_acquisition, 2),
                               'type': 'equity'}
                    
                    equity_tenant += np.round(this_monthly_acquisition, 2)
                    equity_financier -= np.round(this_monthly_acquisition, 2)
                    
                    this_tx['equity_tenant'] = equity_tenant
                    this_tx['equity_financier'] = equity_financier
                    this_tx['equity_crowd'] = equity_crowd
                    
                    #print(this_tx)
                    
                    df = df.append(this_tx, ignore_index=True)
                    df = df[columns]                    
    
            else:
                
                if np.round(equity_crowd, 2) < np.round(this_monthly_acquisition, 2):
                    this_monthly_acquisition = np.round(equity_crowd, 2)
                    

                this_tx = {'timestamp': first_of_month,
                           'from': 'Tenant',
                           'to': 'Crowd',
                           'amount': np.round(this_monthly_acquisition, 2),
                           'type': 'equity'}

                
                equity_tenant += np.round(this_monthly_acquisition, 2)
                equity_crowd -= np.round(this_monthly_acquisition, 2)
    

                this_tx['equity_tenant'] = equity_tenant
                this_tx['equity_financier'] = equity_financier
                this_tx['equity_crowd'] = equity_crowd
            
                #print(this_tx)
                
                df = df.append(this_tx, ignore_index=True)
                df = df[columns]
            
            
            #%% CROWD SALE

            if np.round(equity_financier, 2) > 0:

                crowd_sale = np.round((house_price / 100) * np.random.randint(-3, 4) + (abs(2019-year)/2) + (month**0.5), 2)
                
                if crowd_sale < 0:
                    crowd_sale = 0
                
                
                if np.round(equity_financier, 2) < crowd_sale:
                    crowd_sale = np.round(equity_financier, 2)
                    
                    
                
                equity_financier -= crowd_sale
                equity_crowd += crowd_sale
                
                
                random_date = str(year) + '-' + str(month).rjust(2, '0') + '-' + str(int(np.random.randint(1, 28))).rjust(2, '0')
                
                this_tx = {'timestamp': random_date,
                           'from': 'Crowd',
                           'to': 'Financier',
                           'amount': crowd_sale,
                           'type': 'equity'}
            
                this_tx['equity_tenant'] = equity_tenant
                this_tx['equity_financier'] = equity_financier
                this_tx['equity_crowd'] = equity_crowd
                
                #print(this_tx)
                
                df = df.append(this_tx, ignore_index=True)
                df = df[columns]

            
            
            #%% PRINT VALUES
            
            
# =============================================================================
#             print('month:', months_elapsed)
#             print('this_owned_percent:', this_owned_percent)
#             print('this_monthly_rent:', this_monthly_rent)
#             print('this_monthly_acquisition:', this_monthly_acquisition)
#             #print('paid_this_year:', paid_this_year)
#             print('total_rent:', total_rent)
#             print('equity_tenant:', equity_tenant)
#             print('equity_financier:', equity_financier)
#             print('equity_crowd:', equity_crowd)
#             print('total_paid:', total_paid)
#             print('house price:', house_price)
#             
#             print()
#             print(np.round(equity_tenant, 2) < np.round(house_price, 2))
#             print()
#             print()
# =============================================================================
            
            
            
            this_monthly_rent = this_monthly_rent * 2
            
            months_elapsed = months_elapsed+1

        year += 1
    

# =============================================================================
#     plt.figure()
#     plt.plot(list(range(months_elapsed-1)), rent_over_time)
#     plt.show()
#     
#     
#     plt.figure()
#     plt.plot(list(range(months_elapsed-1)), np.cumsum(rent_over_time))
#     plt.show()
#     
#     
#     plt.figure()
#     plt.plot(list(range(months_elapsed-1)), acquisition_over_time)
#     plt.show()
#     
#     
#     plt.figure()
#     plt.plot(list(range(months_elapsed-1)), np.cumsum(acquisition_over_time) + deposit_amount)
#     plt.ylim([0, house_price*1.1])
#     plt.show()
# =============================================================================

    
    return df

transactions = txdf()

transactions['amount'] = transactions['amount'].apply(lambda x: str(np.round(x, 2)))
transactions['equity_tenant'] = transactions['equity_tenant'].apply(lambda x: str(np.round(x, 2)))
transactions['equity_financier'] = transactions['equity_financier'].apply(lambda x: str(np.round(x, 2)))
transactions['equity_crowd'] = transactions['equity_crowd'].apply(lambda x: str(np.round(x, 2)))

#%%

layout_top = html.Div(
    
    html.Div([
        
        html.Div([
            #html.Img(),
            html.H5('BRICKSONBLOCKS')
        ],
        className='two columns',
        style={'font-weight': 'bold'},

        ),
        
        html.Div([
            html.H5('Wallet Balance: 21652')
        ],
        className='six columns',
        style={'margin-left':'0%'}
        ),

        html.Div([
            html.H5('Maximus')
        ],
        className='two columns',
        style={'width':'12%'},
        ),
        
    ],
    className='row',
    style={'font-family': 'Cerebri Sans',
           'font-weight':'bold',
           'margin-left':'0%'},
    )

)


layout_top = html.Div(
    
    html.Img(
        src=app.get_asset_url('topbar.png')
    )

)




layout_sidebar = html.Div([
    
    html.Div([
        html.Div(children='NAVIGATION',
                 style={'font-size':16,
                        'margin-top': 25,
                        'margin-left': 30}),


        html.Div([
            dcc.Link(children='Home',
                     href='/home',
                     style={'font-size':16,
                            'margin-top': 12,
                            'margin-left': 30,
                            'color':'#696969',
                            'text-decoration': 'none'}),
        ],
        style={'margin-top':12}
        ),

        html.Div([
            dcc.Link(children='Dashboard',
                     href='/investor-dashboard',
                     style={'font-size':16,
                            'margin-top': 12,
                            'margin-left': 30,
                            'color':'#696969',
                            'text-decoration': 'none'}),
        ],
        style={'margin-top':12}
        ),
        

        html.Div([
            dcc.Link(children='Market',
                     href='/browse-listings',
                     style={'font-size':16,
                            'margin-top': 12,
                            'margin-left': 30,
                            'color':'#696969',
                            'text-decoration': 'none'}),
        ],
        style={'margin-top':12}
        ),
        
        

        
        html.Div(children='Residential (372)',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),
        
        html.Div(children='Commercial (116)',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),
        
        html.Div(children='Industrial (53)',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),
        
        html.Div(children='Vacation (92)',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),
        
        html.Div(children='Land (76)',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),
        
        html.Div(children='REITs/Funds (8)',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),
        

        html.Div(children='Manage Funds',
                 style={'font-size':16,
                        'margin-top': 12,
                        'margin-left': 30}),
        
        html.Div(children='Acquire',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),
        
        html.Div(children='Rebalance',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),
        
        html.Div(children='Dispose',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),

        html.Div(children='Automate',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60}),


        html.Div(children='Smart Contracts',
                 style={'font-size':16,
                        'margin-top': 12,
                        'margin-left': 30}),
        

        html.Div([
            dcc.Link(children='Inspect',
                     href='/ownership',
                     style={'font-size':12,
                            'color':'#696969',
                            'text-decoration': 'none'}),
        ],
        style={'margin-top':6,
               'margin-left': 60,}
        ),


# =============================================================================
#         html.Div(children='Inspect',
#                  style={'font-size':12,
#                         'margin-top': 6,
#                         'margin-left': 60}),
# =============================================================================
        
        html.Div([
            dcc.Link(children='Generate',
                     href='/generate-contract',
                     style={'font-size':12,
                            'color':'#696969',
                            'text-decoration': 'none'}),
        ],
        style={'margin-top':6,
               'margin-left': 60,}
        ),

# =============================================================================
#         html.Div(children='Generate',
#                  style={'font-size':12,
#                         'margin-top': 6,
#                         'margin-left': 60}),
# =============================================================================
        
        html.Div(children='Interact',
                 style={'font-size':12,
                        'margin-top': 6,
                        'margin-left': 60,
                        'margin-bottom':1000}),

        
    ],
    
# =============================================================================
#     className='two columns',
#     style={'width': '8%',
#            'font-family': 'Cerebri Sans',
#            'font-weight': 'bold',
#            'color': '#696969',
#            'background-color': '#F0F0F0',
#            'margin-bottom': 1000,
#            'margin-left': 0},
# =============================================================================
    ),
    ],
    className='two columns',
    style={'width': '12%',
           'font-family': 'Cerebri Sans',
           'font-weight': 'bold',
           'color': '#696969',
           'background-color': '#f8f8f8',
           'margin-left': 0,
           'margin-right': 0,},

)




#%%

layout_ownership = html.Div(
    html.Div([


        #Top row, identifiers
        layout_top,
        
        layout_sidebar,
        
        
        html.Div([
            
            html.Div([
                                    
                html.Div([
                    html.H5(
                        children='Ownership',
                        style={'font-weight': 'bold',}
                    ),
                ],
                className='nine columns',
                style={'margin-left':30},
                ),
                
                html.Div([
                    html.Img(
                        src=app.get_asset_url('calendar.png')
                    ),
                ],
                className='three columns',
                style={'float':'right',
                       'margin-left':10,
                       'margin-right':0},
                ),
                
            ],
                
            className='row',
            style={'margin-top':30,
                   'margin-bottom':30},
            ),
    
# =============================================================================
#             html.Div(
#                 #dcc.Link('Go to Page 1', href='/page-1'),
#                 dcc.Link('Go back to home', href='/'),
#             ),    
# =============================================================================
    
    
            #fifth row, stacked area graphs
            html.Div([
    
                #label_compare_graph
                html.Div([
                        
                    dcc.Graph(
                        id='p1-stacked',
                    ),
                                
                ],
                className = 'eight columns',
                style = {'margin-left': 30,
                         'width':'63.2%'},
                ),
    
    
                    #label_compare_graph
                html.Div([
                        
                    dcc.Graph(
                        id='p1-donut',
                    ),
                    
                ],
                className = 'four columns',
                style = {'margin-left': 30,
                         },
                ),
    
            ],
            className = 'row',
            style={'font-family': 'Cerebri Sans',}
            ),
    
    
            html.Div([
                                    
                html.Div([
                    html.H5(
                        children='Smart Contract Transactions',
                        style={'font-weight': 'bold',}
                    ),
                ],
                className='nine columns',
                style={'margin-left':30},
                ),
                
                
            ],
                
            className='row',
            style={'margin-top':30,
                   'margin-bottom':30},
            ),
    
        
            #fifth row, stacked area graphs
            html.Div([
    
                #label_compare_graph
                html.Div([
                        
                    dash_table.DataTable(
                        id='p1-table',
                        columns=[{"name": i, "id": i} for i in transactions.columns],
                        data=transactions.to_dict(orient='records'),
                        style_table={
                            'maxHeight': '1000px',
                            'overflowY': 'scroll'
                        },
                        style_as_list_view=True,
                        filter_action="native",
                        fixed_rows={
                            'headers': True,
                            'data': 0
                        },
                    ),
                    
                ],
                className = 'twelve columns',
                style={'width':'97.5%'}
                ),
        
            ],
            className = 'row',
            style = {'margin-top':30,
                     'margin-left':30}
            ),
        
        
    
            html.Div([
    
                html.Div([
                    dcc.Input(
                        id='p1-nonsense',
                        type='text',
                        value='useless input for enabling callback prototyping',
                    ),
                                
                    ],
                    className = 'ten columns',
                    style={'margin-top':1000}
                ),
    
                ], className = 'row',
            ),   
            
        ],
        className='ten columns',
        style={'font-family': 'Cerebri Sans',
               'background-color': '#e8e8e8',
               'margin-left':0,
               'width':'88%'}
        ),    

        ], className='row',
        style={'font-family': 'Cerebri Sans'},
    ),
)



@app.callback(
    Output('p1-stacked', 'figure'),
    [Input('p1-nonsense', 'value'),])
def stacked_chart(nonsense):
        
    
    
    df = txdf()
    df = df[[_ for _ in df.columns if _ not in ['from', 'to', 'amount', 'type']]]
    
    data = []
    
    for entity in df.columns[1:]:
        data.append(
            dict(
                x = df['timestamp'].values,
                y = df[entity].values,
                name = entity,
                mode = 'lines',
                stackgroup = 'one',
                line = {'width': 1},
            )
        )
        
    
    layout = go.Layout(
        title='Asset shares over time',
        showlegend=True,
        font={'family':'Cerebri Sans'},
        yaxis=dict(title='Percentage'),
    )
    
    
    figure = dict(data=data, layout=layout)
    
    return figure



@app.callback(
    Output('hover-data', 'children'),
    [Input('p1-stacked', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)





@app.callback(
    Output('p1-donut', 'figure'),
    [Input('p1-stacked', 'hoverData')])
def donut_data(hoverData):
    
    hover_dict = hoverData    
    
    data=[
        go.Pie(
            values = [_['y'] for _ in hover_dict['points']],
            #labels = [str(_['curveNumber']) for _ in hover_dict['points']],
            labels = ['equity_tenant', 'equity_financier', 'equity_crowd'],
            hole=0.5,
            sort=False,
        ),
    ]
    
    
    layout=go.Layout(
        title='Equity distribution on ' + str(hover_dict['points'][0]['x']),
        font={'family':'Cerebri Sans'},
    )


    figure = dict(data=data, layout=layout)

    return figure


# =============================================================================
# @app.callback(
#     Output('p1-table', 'data'),
#     [Input('p1-nonsense', 'value'),])
# def equity_table(nonsense):
#     
#     df = txdf()
#     
#     
#     return df.to_dict(orient='records')
# =============================================================================

#%%

layout_investor_dashboard = html.Div(
    
    html.Div([
        
        #Top row, identifiers
        layout_top,
        
        layout_sidebar,        

        html.Div([
            

            html.Div([
                                    
                html.Div([
                    html.H5(
                        children='Dashboard',
                        style={'font-weight': 'bold',}
                    ),
                ],
                className='nine columns',
                style={'margin-left':30},
                ),
                
                html.Div([
                    html.Img(
                        src=app.get_asset_url('calendar.png')
                    ),
                ],
                className='three columns',
                style={'float':'right',
                       'margin-left':10,
                       'margin-right':0},
                ),
                
            ],
                
            className='row',
            style={'margin-top':30,
                   'margin-bottom':30},
            ),
            
            
            
            
            #overview
            html.Div([
                
                html.Div([
                    
                    html.Div([
                    
                        html.H6(
                            children='72,163',
                            style={'font-size':26,
                                   'font-weight': 'bold'}
                        ),
                        html.H6(
                            children='Asset Value',
                            style={'font-weight': 'bold',
                                   'color': '#909090'}
                        ),
                    ],
                    style={'text-align':'right',
                           'margin-right':30},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,
                       'width': '22.7%',
                       'background-color':'#ffffff'},
                ),

                
                html.Div([
                    
                    html.Div([
                    
                        html.H6(
                            children='293.74%',
                            style={'font-size':26,
                                   'font-weight': 'bold'}
                        ),
                        html.H6(
                            children='Return to Date',
                            style={'font-weight': 'bold',
                                   'color': '#909090'}
                        ),
                    ],
                    style={'text-align':'right',
                           'margin-right':30},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,
                       'width': '22.7%',
                       'background-color':'#ffffff'},
                ),
                
                
                html.Div([
                    
                    html.Div([
                    
                        html.H6(
                            children='829',
                            style={'font-size':26,
                                   'font-weight': 'bold'}
                        ),
                        html.H6(
                            children='Number of Investments',
                            style={'font-weight': 'bold',
                                   'color': '#909090'}
                        ),
                    ],
                    style={'text-align':'right',
                           'margin-right':30},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,
                       'width': '22.7%',
                       'background-color':'#ffffff'},
                ),
            
                
                html.Div([
                    
                    html.Div([
                    
                        html.H6(
                            children='17',
                            style={'font-size':26,
                                   'font-weight': 'bold'}
                        ),
                        html.H6(
                            children='Watchlist',
                            style={'font-weight': 'bold',
                                   'color': '#909090'}
                        ),
                    ],
                    style={'text-align':'right',
                           'margin-right':30},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,
                       'width': '22.7%',
                       'background-color':'#ffffff'},
                ),


            ],
                
            className='row',
            style={'margin-top':30,
                   'margin-bottom':30},
            ),
            
            #charts row 1
            html.Div([
    
                #aggregate_performance
                html.Div([
                    dcc.Graph(
                        figure = go.Figure(
                            data=[
                                go.Scatter(
                                    x=pd.date_range(datetime.date(2017, 7, 15), periods=1001).tolist(),
                                    y=np.cumsum(2*np.random.binomial(1, 0.53, 1001)-1)*5+100,
                                    mode='lines',
                                    fill='tozeroy',
                                    hoveron='points+fills',
                                    marker={'color':'#3898ff'},
                                ),
                            ],
                            layout=go.Layout(
                                title='Aggregate Performance',
                                font={'family':'Cerebri Sans'},
                                plot_bgcolor='#ffffff',
                                xaxis={'title':'Date',
                                       'gridcolor':'#e0e0e0'},
                                yaxis={'title':'Gain/Loss',
                                       'gridcolor':'#e0e0e0'},
# =============================================================================
#                                 margin=dict(
#                                     l=20,
#                                     r=20,
#                                     b=20,
#                                     t=20,
#                                     pad=0
#                                 ),
# =============================================================================
                            ),
                        ),
                    ),
                ],
                className='eight columns',
                style={'width':'60%',
                       'margin-left': 30},
                ), 
    
    
                #predictions_vs_actuals
                html.Div([
                    dcc.Graph(
                        figure = go.Figure(
                            data=[
                                go.Bar(
                                    name='Predicted',
                                    x=['Jan',
                                       'Feb',
                                       'Mar',
                                       'Apr',
                                       'May',
                                       'Jun',
                                       'Jul',
                                       'Aug',
                                       'Sep',
                                       'Oct',
                                       'Nov',
                                       'Dec'],
                                    y=[76, 87, 112, 105, 116, 125, 131, 117, 121, 117, 123, 96],
                                    width=[0.25]*12,
                                    marker={'color':'#98fb98'},
                                ),
                                go.Bar(
                                    name='Actual',
                                    x=['Jan',
                                       'Feb',
                                       'Mar',
                                       'Apr',
                                       'May',
                                       'Jun',
                                       'Jul',
                                       'Aug',
                                       'Sep',
                                       'Oct',
                                       'Nov',
                                       'Dec'],
                                    y=[86, 82, 95, 91, 124, 118, 134, 129, 124, 131, 116, 109],
                                    width=[0.25]*12,
                                    marker={'color':'#2e8b57'}
                                )
                            ],
                            layout=go.Layout(
                                title='Projections Vs Actuals',
                                xaxis={'title':'Month',},
                                yaxis={'title':'Return',},
                                font={'family':'Cerebri Sans'},
                                plot_bgcolor='#ffffff',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                            )
                        )
                    ),
                ],
                className = 'four columns',
                style={'width':'34.4%',
                       'margin-left':30},
                ), 
    
            ],
            className='row'
            ),
    
            #charts row 2
            html.Div([
    
    
    
                #label_compare_graph
                html.Div([
                    dcc.Graph(
                        figure = go.Figure(
                            data=[
                                go.Bar(
                                    name='Appreciation',
                                    x=['2016',
                                       '2017',
                                       '2018',],
                                    y=[89, 73, 98],
                                    marker={'color':['#0069a6']*3}
                                ),
                                go.Bar(
                                    name='Rental',
                                    x=['2016',
                                       '2017',
                                       '2018',],
                                    y=[26, 54, 62],
                                    marker={'color':['#18d6e8']*3}
                                ),
                                go.Bar(
                                    name='Fees',
                                    x=['2016',
                                       '2017',
                                       '2018',],
                                    y=[22, 13, 15],
                                    marker={'color':['#828fff']*3}
                                ),
                                go.Bar(
                                    name='',
                                    x=['2018',],
                                    y=[30],
                                    marker={'color':['#ffffff']*3}
                                ),
                            ],
                            layout=go.Layout(
                                title='Revenue Split',
                                font={'family':'Cerebri Sans'},
                                barmode='stack',
                                xaxis={'title':'Year'},
                                yaxis={'title':'Income'},
                                plot_bgcolor='#ffffff',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.12
                                ),
                            )
                        )
                    ),
                ],
                className = 'three columns',
                style={'margin-left': 30},
                ), 
    
    
                #label_compare_graph
                html.Div([
                    dcc.Graph(
                        figure = go.Figure(
                            data=[
                                go.Pie(
                                    labels=['Residential',
                                            'Commercial',
                                            'Industrial',
                                            'Vacation',
                                            'Land',
                                            'REITs/Funds'],
                                    values=[142, 72, 17, 23, 46, 89],
                                    hole=0.6,
                                ),
                            ],
                            layout=go.Layout(
                                title='Portfolio Breakdown',
                                font={'family':'Cerebri Sans'},
                                legend=go.layout.Legend(
                                    x=1,
                                    y=0.5
                                ),
                            )
                        )
                    ),
                ],
                className = 'four columns',
                style={'margin-left': 30},
                ), 
    
    
                #label_compare_graph
                html.Div([
                    dcc.Graph(
                        figure = go.Figure(
                            data = [
                                go.Scattermapbox(
                                    lat=capitals['Latitude'],
                                    lon=capitals['Longitude'],
                                    mode='markers',
                                    marker=go.scattermapbox.Marker(
                                        size=9
                                    ),
                                    #text=capitals['Capital'],
                                    text=[f"City: {i} <br>Country: {j}" for i,j in zip(capitals['Capital'], capitals['Country'])],
                                ),
                            ],
                            
                            layout=go.Layout(
                                title='Property Locations',
                                font={'family':'Cerebri Sans'},
                                autosize=True,
                                hovermode='closest',
                                mapbox=dict(
                                    accesstoken=mapbox_access_token,
                                    bearing=0,
                                    center=dict(
                                        lat=15,
                                        lon=5,
                                        ),
                                    pitch=0,
                                    zoom=0,
                                ),
                            ),
                        ),

                    ),
                ],
                className = 'five columns',
                style={'margin-left': 30,
                       'width':'40%'},
                ), 
    
    
            ],
            className='row',
            style={'margin-top': 30,
                   'margin-bottom': 30,},
            ),

        ],
        className='ten columns',
        style={'font-family': 'Cerebri Sans',
               'background-color': '#e8e8e8',
               'margin-left':0,
               'width':'88%'}
        ),

        
    ],
    ),
    style={'font-family': 'Cerebri Sans',
           'background-color': '#c0c0c0',}

)

#%%


layout_listings = html.Div(
    
    html.Div([
        
        #Top row, identifiers
        layout_top,
        
        layout_sidebar,        

        html.Div([
            

            html.Div([
                                    
                html.Div([
                    html.H5(
                        children='Listings',
                        style={'font-weight': 'bold',}
                    ),
                ],
                className='nine columns',
                style={'margin-left':30},
                ),
                
                html.Div([
                    html.Img(
                        src=app.get_asset_url('calendar.png')
                    ),
                ],
                className='three columns',
                style={'float':'right',
                       'margin-left':10,
                       'margin-right':0},
                ),
                
            ],
                
            className='row',
            style={'margin-top':30,
                   'margin-bottom':30},
            ),
            

            html.Div([
                
                html.Div([
                    
                    html.Div([
                        
# =============================================================================
#                         html.H5(
#                             children='Listing1',
#                         ),
# =============================================================================
                        html.Img(
                            src=app.get_asset_url('tomoaki_house.png')
                        )
                        
                    ],
                    style={'background-color':'#ffffff'},
                    ),
                    
                ],
                
                className='six columns',
                style={'margin-left':30,},
                ),



                html.Div([
                    
                    html.Div([
                        
# =============================================================================
#                         html.H5(
#                             children='Listing2',
#                         ),
# =============================================================================

                        html.Img(
                            src=app.get_asset_url('mount_isulbrostur.png')
                        ),

                    ],
                    style={'background-color':'#ffffff'},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,},
                ),



                html.Div([
                    
                    html.Div([
                        
# =============================================================================
#                         html.H5(
#                             children='Listing3',
#                         ),
# =============================================================================
                        html.Img(
                            src=app.get_asset_url('eagle_ranch.png')
                        ),
                        
                    ],
                    style={'background-color':'#ffffff'},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,},
                ),

            ],
                
            className='row',
            style={'margin-bottom':30},
            ),
        


            html.Div([
                
                html.Div([
                    
                    html.Div([
                        
# =============================================================================
#                         html.H5(
#                             children='Listing3',
#                         ),
# =============================================================================
                        html.Img(
                            src=app.get_asset_url('hex_machinery.png')
                        ),
                        
                    ],
                    style={'background-color':'#ffffff'},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,},
                ),



                html.Div([
                    
                    html.Div([
                        
# =============================================================================
#                         html.H5(
#                             children='Listing3',
#                         ),
# =============================================================================
                        html.Img(
                            src=app.get_asset_url('cyclotron_arch.png')
                        ),
                        
                    ],
                    style={'background-color':'#ffffff'},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,},
                ),



# =============================================================================
#                 html.Div([
#                     
#                     html.Div([
#                         html.H5(
#                             children='Listing6',
#                         ),
#                     ],
#                     style={'background-color':'#ffffff'},
#                     ),
#                     
#                 ],
#                 
#                 className='three columns',
#                 style={'margin-left':30,},
#                 ),
# 
# 
#                 html.Div([
#                     
#                     html.Div([
#                         html.H5(
#                             children='Listing7',
#                         ),
#                     ],
#                     style={'background-color':'#ffffff'},
#                     ),
#                     
#                 ],
#                 
#                 className='three columns',
#                 style={'margin-left':30,},
#                 ),
# =============================================================================


            ],
                
            className='row',
            style={'margin-bottom':30},
            ),





        ],
        className='ten columns',
        style={'font-family': 'Cerebri Sans',
               'background-color': '#f0f0f0',
               'margin-left':0,
               'width':'88%'}
        ),

        
    ],
    ),
    style={'font-family': 'Cerebri Sans',
           'background-color': '#c0c0c0',}

)


#%%




layout_generate_contract = html.Div(
    
    html.Div([
        
        #Top row, identifiers
        layout_top,
        
        layout_sidebar,        

        html.Div([
            

            html.Div([
                
                html.Div([
                    
                    html.Div([
                        html.H5(
                            children='Generate Contract',
                            style={'font-weight':'bold'}
                        ),
                    ],
                    style={},
                    ),
                    
                ],
                
                className='three columns',
                style={'margin-left':30,},
                ),


            ],
                
            className='row',
            style={'margin-top':30,
                   'margin-bottom':30},
            ),
            

            html.Div([
                
                html.Div([
                    
                    html.Div([
                        
                        html.Div([
                            html.H4('Contract Name:'),
                        ],
                        className='six columns',
                        ),
                        
                        
                        html.Div([
                            dcc.Input(
                                id='contract-name'
                            ),
                        ],
                        className='six columns',
                        )
                        
                    ],
                    className='row',
                    ),

                    html.Div([
                        
                        html.Div([
                            html.H4('Financier Address:'),
                        ],
                        className='six columns',
                        ),
                        
                        
                        html.Div([
                            dcc.Input(
                                id='financier-address'
                            ),
                        ],
                        className='six columns',
                        )
                        
                    ],
                    className='row',
                    ),

                    
                ],
                
                className='six columns',
                style={'margin-left':30,
                       'background-color':'#ffffff'},
                ),



            ],
                
            className='row',
            style={'margin-bottom':30},
            ),
        


            html.Div([
                
                html.Div([
                    
                    html.Div([
                        
                                            
                        dcc.Markdown(
                            id='smart-contract',
                        )
                        
                    ],
                    style={'background-color':'#ffffff'},
                    ),
                    
                ],
                
                className='eleven columns',
                style={'margin-left':30,},
                ),



            ],
                
            className='row',
            style={'margin-bottom':30},
            ),





        ],
        className='ten columns',
        style={'font-family': 'Cerebri Sans',
               'background-color': '#f0f0f0',
               'margin-left':0,
               'width':'88%'}
        ),

        
    ],
    ),
    style={'font-family': 'Cerebri Sans',
           'background-color': '#c0c0c0',}

)


@app.callback(Output('smart-contract', 'children'),
              [Input('contract-name', 'value')])
def generate_smart_contract(contract_name):
    
    if contract_name == None:
        contract_name = ''
    
    instantiate_class = f'class {contract_name}(sp.Contract):'
    
    initialisation = f'''
        def __init__(self,
                     house_price,
                     deposit_amount,
                     tenant_address,
                     financier_address):
    
            self.init(house_price = house_price,
                      equity_tenant = deposit_amount,
                      equity_financier = house_price - deposit_amount,
                      equity_crowd = 0,
                      rent_received_financier = 0,
                      rent_received_crowd = 0,
                      tenant_address = tenant_address,
                      financier_address = financier_address,
                      crowd_addresses = [],
                      crowd_equities = [],
                      crowd_rents = [])
    '''


# =============================================================================
#     test_addreesses = f'''
#         tenant_address = sp.address("{tenant_address}")
#         financier_address = sp.address("{financier_address}")
#         crowd_address_1 = sp.address("tz1c")
#         crowd_address_2 = sp.address("tz2c")
#         crowd_address_3 = sp.address("tz3c")
#     '''
# =============================================================================



    
    code = f'''
    ```py
    
    import smartpy as sp
    
    {instantiate_class}
    {initialisation}
    
    
    
    @sp.add_test(name="test_{contract_name}")
    def test_{contract_name}():
        scenario = sp.test_scenario()
        scenario.h1("Testing Smart Contract {contract_name}")


    


    contract = House_123456789(house_price=200000,
                               deposit_amount=30000,
                               tenant_address=tenant_address,
                               financier_address=financier_address)

    
    ```
    '''
    
    
    code = f'''
    ```py
    
    
    import smartpy as sp
    
    
    
    class House_123456789(sp.Contract):
    
    
        def __init__(self,
                     house_price,
                     deposit_amount,
                     base_rent,
                     tenant_address,
                     financier_address):
    
            self.init(house_price = house_price,
                      equity_tenant = deposit_amount,
                      equity_financier = house_price - deposit_amount,
                      equity_crowd = 0,
                      base_rent=base_rent,
                      rent_received_financier = 0,
                      rent_received_crowd = 0,
                      tenant_address = tenant_address,
                      financier_address = financier_address,
                      crowd_addresses = [],
                      crowd_equities = [],
                      crowd_rents = [])
    
    
        #%%
        
        def div(a, b):
            return sp.nat(((a * 1000000000) // b) // 1000000000)
    
        
        @sp.entry_point
        def tenant_rental_payment_to_financier(self, params):
            
            sp.verify(sp.sender == self.data.tenant_address)
            
            sp.if self.data.equity_financier > 0:
                self.data.rent_received_financier += abs(params.amount) * (self.data.equity_financier * 1000000 // self.data.house_price) // 1000000
    
                
        @sp.entry_point
        def tenant_rental_payment_to_crowd(self, params):
            sp.if self.data.equity_crowd > 0:
                self.data.rent_received_crowd += abs(params.amount) * (self.data.equity_crowd * 1000000 // self.data.house_price) // 1000000
    
    
        @sp.entry_point
        def tenant_rental_payment_to_all_crowd(self, params):
    
            sp.if self.data.equity_crowd > 0:
                self.data.rent_received_crowd += abs(params.amount) * (self.data.equity_crowd * 1000000 // self.data.house_price) // 1000000
    
                self.data.crowd_equities = self.data.crowd_equities.rev()
    
                sp.for each_equity in self.data.crowd_equities:
                    self.data.crowd_rents.push(1 * (each_equity * self.data.base_rent * 1000000000 // self.data.house_price) // 1000000000)
    
                #sp.for i in sp.range(0, sp.len(self.data.crowd_equities)):
                #    self.data.crowd_rents[i] += i+7
    
                self.data.crowd_equities = self.data.crowd_equities.rev()
    
    
        @sp.entry_point
        def tenant_rental_payment_to_everyone(self, params):
            sp.if self.data.equity_financier > 0:
                self.data.rent_received_financier += abs(params.amount) * (self.data.equity_financier * 1000000 // self.data.house_price) // 1000000
            sp.if self.data.equity_crowd > 0:
                self.data.rent_received_crowd += abs(params.amount) * (self.data.equity_crowd * 1000000 // self.data.house_price) // 1000000
    
        #%%
    
        @sp.entry_point
        def equity_from_financier_to_tenant(self, params):
            self.data.equity_tenant += params.amount
            sp.if self.data.equity_financier >= params.amount:
                self.data.equity_financier = abs(self.data.equity_financier - params.amount)
    
    
        @sp.entry_point
        def equity_from_financier_to_crowd(self, params):
            sp.if self.data.equity_financier >= params.amount:
                self.data.equity_crowd += params.amount
                self.data.equity_financier = abs(self.data.equity_financier - params.amount)
    
    
        @sp.entry_point
        def equity_from_crowd_to_tenant(self, params):
            sp.if self.data.equity_crowd >= params.amount:
                self.data.equity_tenant += params.amount
                self.data.equity_crowd = abs(self.data.equity_crowd - params.amount)
    
        #%%
    
        @sp.entry_point
        def add_new_crowd_address(self, params):
            self.data.crowd_addresses.push(sp.sender)
            self.data.crowd_equities.push(params.acquisition)
            self.data.crowd_rents.push(0)
            self.data.equity_crowd += params.acquisition
            self.data.equity_financier = sp.as_nat(self.data.equity_financier - params.acquisition)
    
        #%%
    
    
    
    @sp.add_test(name="testingposting")
    def test():
        scenario = sp.test_scenario()
        scenario.h1("Test")
    
        tenant_address = sp.address("tz1")
        financier_address = sp.address("tz2")
        crowd_address_1 = sp.address("tz1c")
        crowd_address_2 = sp.address("tz2c")
        crowd_address_3 = sp.address("tz3c")
    
    
        contract = House_123456789(house_price=200000,
                                   deposit_amount=30000,
                                   base_rent=1000,
                                   tenant_address=tenant_address,
                                   financier_address=financier_address)
    
        scenario += contract
    
    
        test_purchases=True
        test_rents = True
        test_crowd_sale = True
    
    
        if test_purchases == True:
    
            scenario.h2("tenant buys from financier")
            scenario += contract.equity_from_financier_to_tenant(amount=abs(1000)).run(sender=tenant_address)
    
            scenario.h2("crowd buys from financier")
            scenario += contract.equity_from_financier_to_crowd(amount=abs(2000)).run(sender=tenant_address)
    
            scenario.h2("tenant buys from crowd")
            scenario += contract.equity_from_crowd_to_tenant(amount=abs(1000)).run(sender=tenant_address)
    
    
        if test_rents == True:
    
            scenario.h2("tenant pays rent to financier")
            scenario += contract.tenant_rental_payment_to_financier(amount=abs(1000)).run(sender=tenant_address)
    
            scenario.h2("tenant pays rent to crowd")
            scenario += contract.tenant_rental_payment_to_crowd(amount=abs(1000)).run(sender=tenant_address)
    
            scenario.h2("tenant pays rent to everyone")
            scenario += contract.tenant_rental_payment_to_everyone(amount=abs(1000)).run(sender=tenant_address)
    
    
        if test_crowd_sale == True:
            scenario.h2("random person 1 buys some house")
            scenario += contract.add_new_crowd_address(acquisition=2000).run(sender=crowd_address_1)
            scenario.h2("random person 2 buys some house")
            scenario += contract.add_new_crowd_address(acquisition=7000).run(sender=crowd_address_2)
            scenario.h2("random person 3 buys some house")
            scenario += contract.add_new_crowd_address(acquisition=4000).run(sender=crowd_address_3)
            
        scenario.h2("tenant pays rent to all crowd")
        scenario += contract.tenant_rental_payment_to_all_crowd(amount=10000).run(sender=tenant_address)
        
        
    


    
    ```
    '''
    
    
    return code
    



#%%



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/ownership':
        return layout_ownership
    elif pathname == '/investor-dashboard':
        return layout_investor_dashboard
    elif pathname == '/browse-listings':
        return layout_listings
    elif pathname == '/generate-contract':
        return layout_generate_contract
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)


