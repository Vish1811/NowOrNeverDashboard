import dash
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash('NowOrNever',external_stylesheets=external_stylesheets)
colors={'background':'#111111',
'text':'#7FDBFF'}

server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'NowOrNeverProgressTracker'


#layout.py

app.layout=html.Div(children=[
    html.H1(children='NowOrNever Dashboard',style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div(children='A web Application for tracking progress of the students',style={
        'textAlign': 'center',
        'color': colors['text']
    })
])


if __name__=='__main__':
    app.run_server(debug=True)