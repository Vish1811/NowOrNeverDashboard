import dash
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash('NowOrNever',external_stylesheets=external_stylesheets)
colors={'background':'#111111',
'text':'blue'}
tabs_styles = {
    'height': '51px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '2px',
    'fontWeight': 'bold',
    'vertical-align': 'middle',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'white',
    'color': 'blue',
    'padding': '10px',
    "font-size": 20
}

server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'NowOrNeverProgressTracker'


#layout.py

app.layout=html.Div(children=[
    html.H1(children='NowOrNever Dashboard',style={
        'textAlign': 'center',
        'color': colors['text'],
        'background':"lightgreen"
    }),
    html.Div(children='A web Application for tracking progress of the students',style={
        'textAlign': 'center',
        'color': colors['text']
    })
])


if __name__=='__main__':
    app.run_server(debug=True)