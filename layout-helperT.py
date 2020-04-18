import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, id='main', children=[
    html.H1(
        children='Now and Never Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text'],

        }
    ),
    html.P(children='Introduction to now and never',style={
            'textAlign': 'center',
            'color': colors['text'],
        }),

    html.Table(style={
            'color': colors['text'],
            'border': '1'
        },
        children=[
        html.Thead(
            html.Tr([html.Th(children='Select the team to check the progress', colSpan='16')])
        ),
        html.Div(id ='t1',children=[ html.Tbody([
            html.Tr([
                html.Td('Team Name: Code_to_death'),
                html.Td('Members: Ashish Ranjan, Tooba Zameer, Vishnu Kumar, Yohansh Gupta'),
                html.Td('Mentor Name: Pta nhi kb assign hnge :| '),
                html.Td(children=[html.Div([html.Button('Progress', id='team1', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t2', children=[ html.Tr([
                html.Td('Team Name: ABC'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team2', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t3', children=[ html.Tr([
                html.Td('Team Name: XYZ'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team3', n_clicks=0)]
                    )])

            ])]),
        html.Div(id='t4', children=[ html.Tr([
                html.Td('Team Name: ABC'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team4', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t5', children=[  html.Tr([
                html.Td('Team Name: XYZ'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team5', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t6', children=[ html.Tr([
                html.Td('Team Name: XYZ'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team6', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t7', children=[ html.Tr([
                html.Td('Team Name: XYZ'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team7', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t8', children=[ html.Tr([
                html.Td('Team Name: XYZ'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team8', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t9', children=[ html.Tr([
                html.Td('Team Name: XYZ'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team9', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t10', children=[ html.Tr([
                html.Td('Team Name: XYZ'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team10', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t11', children=[ html.Tr([
                html.Td('Team Name: XYZ'),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team11', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t12', children=[ html.Tr([
                html.Td('Team Name: XYZ '),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team12', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t13', children=[ html.Tr([
                html.Td('Team Name: XYZ '),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team13', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t14', children=[ html.Tr([
                html.Td('Team Name: XYZ '),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team14', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t15', children=[ html.Tr([
                html.Td('Team Name: XYZ '),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team15', n_clicks=0)]
                    )])
            ])]),
        html.Div(id='t16', children=[ html.Tr([
                html.Td('Team Name: XYZ '),
                html.Td('Members: M1 M2 M3 M4'),
                html.Td('Mentor Name: ---'),
                html.Td(children=[html.Div([html.Button('Progress', id='team16', n_clicks=0)]
                    )])
            ])])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)