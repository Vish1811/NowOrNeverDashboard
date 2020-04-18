import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly
import pandas as pd

app = dash.Dash()
# This is the varialtion which updates on refresh


# This function will get data from extraction
# For now, let's have a 2D array, index of arrai is que
# Array[0] is for time/date of solved que, Array[1] for complexity
# Lets generate a random data for now.

# we will use just -> team_data = extraxt()
from random import randint
ran_comp = ['logn', 'n', 'nlogn', 'n^2', 'n^3']
team_data = [[randint(1, 20) for i in range(15)], [ran_comp[randint(0, 4)] for i in range(15)]]
team_data2 = [[randint(1, 20) for i in range(15)], [ran_comp[randint(0, 4)] for i in range(15)]]
team_data_que_time = team_data[0]; #for line chart
team_data_que_time2 = team_data2[0]
comp_values = [team_data[1].count(complexity) for complexity in ran_comp] #for pie chart
comp_values2 = [team_data2[1].count(complexity) for complexity in ran_comp]
# random team_data generation block end





#https://community.plotly.com/t/two-graphs-side-by-side/5312
#link to troubleshoot problems in display of multiple charts in 1 page


def load_page_layout():
    # Again we will just use team_data = extract()
    team_data = [[randint(1, 20) for i in range(15)], [ran_comp[randint(0, 4)] for i in range(15)]]
    team_data2 = [[randint(1, 20) for i in range(15)], [ran_comp[randint(0, 4)] for i in range(15)]]
    team_data_que_time = team_data[0]; #for line chart
    team_data_que_time2 = team_data2[0]
    comp_values = [team_data[1].count(complexity) for complexity in ran_comp] #for pie chart
    comp_values2 = [team_data2[1].count(complexity) for complexity in ran_comp]
    # random team_data generation block end

    print(team_data[0])
    return html.Div([
            html.Div([
            html.H1(
                children='XYZ data',
                style={
                    'textAlign': 'center',
                    'color': 'black',
                }
            ),
            html.Div([
                html.Label('display-value'),
                    dcc.Dropdown(
                        id='dropdown',
                        options=[
                            {'label': 'Whole Team', 'value': 'TM'},
                            {'label': 'Team Member 1', 'value': 'TM1'},
                            {'label': 'Team Member 2', 'value': 'TM2'},
                            {'label': 'Team Member 3', 'value': 'TM3'},
                            {'label': 'Team Member 4', 'value': 'TM4'},
                        ],
                        value='TM'
                    ),
                    html.Div(id='display-value')
                ],
                style={
                    'textAlign': 'center',
                    'color': 'black',
                }
            ),
            html.Div([
                dcc.Graph(
                    id='que_solved',
                    figure={
                        'data': [
                            {'y' : team_data_que_time, 'type' : 'line'},
                        ],
                        'layout': go.Layout(
                            xaxis={'title' : 'Number of questions'},
                            yaxis={'title' : 'Days'},
                            hovermode='closest'
                        )
                    }
                )
            ], className = "row"),
            html.Div([
                dcc.Graph(
                    id='que_solved_pie',
                    figure={
                        'data': [
                            {'labels' : ran_comp, 'values' : comp_values, 'type' : 'pie'},
                        ],
                        'layout': {
                        }
                    }
                )
            ], className = "row"),
        ])
    ])
'''
app.layout = html.Div([
    dcc.Graph(
        id='que_solved_pie',
        figure={
            'data': [
                {'labels' : ran_comp, 'values' : [5, 3, 8, 15, 4], 'type' : 'pie'},
            ],
            'layout': {
            }
        }
    )
])
'''

app.layout = load_page_layout

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# Below code is for interactivity. 

'''
@app.callback(dash.dependencies.Output('que_solved', 'figure'),
              [dash.dependencies.Input('dropdown', 'value')])
def update_line(value):
    fig = plotly.subplots.make_subplots()
    #print("----------" + str(type(value)))
    if(value == 'TM'):
        fig={
            'data': [
                {'y' : team_data_que_time, 'type' : 'line'},
            ],
            'layout': go.Layout(
                xaxis={'title' : 'Number of questions'},
                yaxis={'title' : 'Days'},
                hovermode='closest'
            )
        }
    else:
        fig={
            'data': [
                {'y' : team_data_que_time2, 'type' : 'line'},
            ],
            'layout': go.Layout(
                xaxis={'title' : 'Number of questions'},
                yaxis={'title' : 'Days'},
                hovermode='closest'
            )
        }

    return fig

@app.callback(dash.dependencies.Output('que_solved_pie', 'figure'),
              [dash.dependencies.Input('dropdown', 'value')])
def update_pie(value):
    fig = plotly.subplots.make_subplots()
    #print("----------" + str(type(value)))
    if(value == 'TM'):
        fig={
            'data': [
                {'labels' : ran_comp, 'values' : comp_values, 'type' : 'pie'},
            ],
            'layout': {
            }
        }
    else:
        fig={
            'data': [
                {'labels' : ran_comp, 'values' : comp_values2, 'type' : 'pie'},
            ],
            'layout': {
            }
        }

    return fig
'''
if __name__ == '__main__':
    app.run_server()
