import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from panels import member1,member2,member3,member4


server = app.server

app.layout = html.Div(
    [
        html.Div(
            className="row header",
            children=[
                html.Button(id="menu", children=dcc.Markdown("&#8801")),
                html.Span(
                    className="app-title",
                    children=[
                        dcc.Markdown("**Code_To_Death**"),
                        
                    ],
                ),
                html.Img(src=app.get_asset_url("logo.png")),
                html.A(
                    id="learn_more",
                    children=html.Button("Learn More"),
                    href="https://plot.ly/dash/",
                ),
            ],
        ),
        html.Div(
            id="tabs",
            className="row tabs",
            children=[
                dcc.Link("Member-1", href="/"),
                dcc.Link("Member-2", href="/"),
                dcc.Link("Member-3", href="/"),
                dcc.Link("Member-4", href="/"),
            ],
        ),
        html.Div(
            id="mobile_tabs",
            className="row tabs",
            style={"display": "none"},
            children=[
                 dcc.Link("Member-1", href="/"),
                dcc.Link("Member-2", href="/"),
                dcc.Link("Member-3", href="/"),
                 dcc.Link("Member-4", href="/"),
            ],
        ),
        dcc.Store(  # opportunities df
            id="opportunities_df",
            #data=sf_manager.get_opportunities().to_json(orient="split"),
        ),
        dcc.Store(  # leads df
            id="leads_df", #data=sf_manager.get_leads().to_json(orient="split")
        ),
        dcc.Store(
            id="cases_df", #data=sf_manager.get_cases().to_json(orient="split")
        ),  # cases df
        dcc.Location(id="url", refresh=False),
        html.Div(id="tab_content"),
        html.Link(
            href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",
            rel="stylesheet",
        ),
        html.Link(
            href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"
        ),
        html.Link(
            href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"
        ),
        html.Link(
            href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"
        ),
    ],
    className="row",
    style={"margin": "0%"},
)

# Update the index


@app.callback(
    [
        Output("tab_content", "children"),
        Output("tabs", "children"),
        Output("mobile_tabs", "children"),
    ],
    [Input("url", "pathname")],
)
def display_page(pathname):
    tabs = [
        dcc.Link("Member-1", href="/dash-salesforce-crm/member1"),
        dcc.Link("Member-2", href="/dash-salesforce-crm/member2"),
        dcc.Link("member-3", href="/dash-salesforce-crm/member3"),
        dcc.Link("Member-4", href="/dash-salesforce-crm/member4"),

    ]
    if pathname == "/dash-salesforce-crm/member1":
        tabs[0] = dcc.Link(
            dcc.Markdown("**&#9632 Member-1**"),
            href="/dash-salesforce-crm/member1",
        )
        return member1.layout, tabs, tabs
    elif pathname == "/dash-salesforce-crm/member2":
        tabs[1] = dcc.Link(
            dcc.Markdown("**&#9632 Member-2**"), href="/dash-salesforce-crm/member2"
        )
        return member2.layout, tabs, tabs
    elif pathname == "/dash-salesforce-crm/member3":
        tabs[2] = dcc.Link(
            dcc.Markdown("**&#9632 Member-3**"), href="/dash-salesforce-crm/member3"
        )
        return member3.layout, tabs, tabs
    else:
        tabs[3] = dcc.Link(
            dcc.Markdown("**&#9632 Member-4**"), href="/dash-salesforce-crm/member4"
        )
        return member4.layout, tabs, tabs


@app.callback(
    Output("mobile_tabs", "style"),
    [Input("menu", "n_clicks")],
    [State("mobile_tabs", "style")],
)
def show_menu(n_clicks, tabs_style):
    if n_clicks:
        if tabs_style["display"] == "none":
            tabs_style["display"] = "flex"
        else:
            tabs_style["display"] = "none"
    return tabs_style


if __name__ == "__main__":
    app.run_server(debug=True)