# -*- coding: utf-8 -*-
from datetime import date
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objs as go

from app import app, indicator, millify, df_to_table#, sf_manager


def converted_opportunities(period, source, df):
    df["CreatedDate"] = pd.to_datetime(df["CreatedDate"], format="%Y-%m-%d")

    # source filtering
    if source == "all_s":
        df = df[df["IsWon"] == 1]
    else:
        df = df[(df["LeadSource"] == source) & (df["IsWon"] == 1)]

    # period filtering
    if period == "W-MON":
        df["CreatedDate"] = pd.to_datetime(df["CreatedDate"]) - pd.to_timedelta(
            7, unit="d"
        )
    df = (
        df.groupby([pd.Grouper(key="CreatedDate", freq=period)])
        .count()
        .reset_index()
        .sort_values("CreatedDate")
    )

    # if no results were found
    if df.empty:
        layout = dict(
            autosize=True, annotations=[dict(text="No results found", showarrow=False)]
        )
        return {"data": [], "layout": layout}

    trace = go.Scatter(
        x=df["CreatedDate"],
        y=df["IsWon"],
        name="converted opportunities",
        fill="tozeroy",
        fillcolor="#e6f2ff",
    )

    data = [trace]

    layout = go.Layout(
        autosize=True,
        xaxis=dict(showgrid=False),
        margin=dict(l=35, r=25, b=23, t=5, pad=4),
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    return {"data": data, "layout": layout}


# returns heat map figure
def heat_map_fig(df, x, y):
    z = []
    for lead_type in y:
        z_row = []
        for stage in x:
            probability = df[(df["StageName"] == stage) & (df["Type"] == lead_type)][
                "Probability"
            ].mean()
            z_row.append(probability)
        z.append(z_row)

    trace = dict(
        type="heatmap", z=z, x=x, y=y, name="mean probability", colorscale="Blues"
    )
    layout = dict(
        autosize=True,
        margin=dict(t=25, l=210, b=85, pad=4),
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    return go.Figure(data=[trace], layout=layout)


# returns top 5 open opportunities
def top_open_opportunities(df):
    df = df.sort_values("Amount", ascending=True)
    cols = ["CreatedDate", "Name", "Amount", "StageName"]
    df = df[cols].iloc[:5]
    # only display 21 characters
    df["Name"] = df["Name"].apply(lambda x: x[:30])
    return df_to_table(df)


# returns top 5 lost opportunities
def top_lost_opportunities(df):
    df = df[df["StageName"] == "Closed Lost"]
    cols = ["CreatedDate", "Name", "Amount", "StageName"]
    df = df[cols].sort_values("Amount", ascending=False).iloc[:5]
    # only display 21 characters
    df["Name"] = df["Name"].apply(lambda x: x[:30])
    return df_to_table(df)



layout = [
    html.Div(
            className="row header1",
            children=[
                html.Span(
                    className="app-title1",
                    children=[
                        dcc.Markdown("Overall Progress"),
                    ],
                ),
            ],
        ),
    html.Div(
        id="opportunity_grid",
        children=[
            html.Div(
                className="control dropdown-styles",
                children=dcc.Dropdown(
                    id="converted_opportunities_dropdown",
                    options=[
                        {"label": "Easy", "value": "D"},
                        {"label": "Medium", "value": "W-MON"},
                        {"label": "Hard", "value": "M"},
                    ],
                    value="D",
                    clearable=False,
                ),
            ),
            
            html.Div(
                className="control dropdown-styles",
                children=dcc.Dropdown(
                    id="converted_opportunities_dropdown",
                    options=[
                        {"label": "Group1", "value": "D"},
                        {"label": "Group2", "value": "D"},
                        {"label": "Group3", "value": "D"},
                        {"label": "Group4", "value": "D"},
                        {"label": "Group5", "value": "D"},
                        {"label": "Group6", "value": "D"},
                        {"label": "Group7", "value": "D"},
                        {"label": "Group8", "value": "D"},
                    ],
                    value="D",
                    clearable=True,
                ),
            ),
            html.Span(
                "See Ranking",
                id="new_opportunity",
                n_clicks=0,
                className="button pretty_container",
            ),
            html.Div(
                id="opportunity_indicators",
                className="row indicators",
                children=[
                    indicator(
                        "#00cc96", "Total Attempted", "left_opportunities_indicator"
                    ),
                    indicator(
                        "#119DFF",
                        "Left problems",
                        "middle_opportunities_indicator",
                    ),
                    indicator(
                        "#00cc96", "Suceesful", "left_opportunities_indicator"
                    ),
                    indicator(
                        "#00cc96", "After Editorial", "left_opportunities_indicator"
                    ),
                    indicator(
                        "#00cc96", "Before Editorial", "left_opportunities_indicator"
                    ),
                ],

            ),
            html.Div(
                id="converted_count_container",
                className="chart_div pretty_container",
                children=[
                    html.P("Graph1"),
                    dcc.Graph(
                        id="converted_count",
                        style={"height": "90%", "width": "98%"},
                        config=dict(displayModeBar=False),
                    ),
                ],
            ),
            html.Div(
                id="opportunity_heatmap",
                className="chart_div pretty_container",
                children=[
                    html.P("Graph2"),
                    dcc.Graph(
                        id="heatmap",
                        style={"height": "90%", "width": "98%"},
                        config=dict(displayModeBar=False),
                    ),
                ],
            ),
            
            
        ],
    ),
]


# # updates heatmap figure based on dropdowns values or df updates
# @app.callback(
#     Output("heatmap", "figure"),
#     [Input("heatmap_dropdown", "value"), Input("opportunities_df", "data")],
# )
# def heat_map_callback(stage, df):
#     df = pd.read_json(df, orient="split")
#     df = df[pd.notnull(df["Type"])]
#     x = []
#     y = df["Type"].unique()
#     if stage == "all_s":
#         x = df["StageName"].unique()
#     elif stage == "cold":
#         x = ["Needs Analysis", "Prospecting", "Qualification"]
#     elif stage == "warm":
#         x = ["Value Proposition", "Id. Decision Makers", "Perception Analysis"]
#     else:
#         x = ["Proposal/Price Quote", "Negotiation/Review", "Closed Won"]
#     return heat_map_fig(df, x, y)


# # updates converted opportunity count graph based on dropdowns values or df updates
# @app.callback(
#     Output("converted_count", "figure"),
#     [
#         Input("converted_opportunities_dropdown", "value"),
#         Input("source_dropdown", "value"),
#         Input("opportunities_df", "data"),
#     ],
# )
# def converted_opportunity_callback(period, source, df):
#     df = pd.read_json(df, orient="split")
#     return converted_opportunities(period, source, df)


# # updates left indicator value based on df updates
# @app.callback(
#     Output("left_opportunities_indicator", "children"),
#     [Input("opportunities_df", "data")],
# )
# def left_opportunities_indicator_callback(df):
#     df = pd.read_json(df, orient="split")
#     won = millify(str(df[df["IsWon"] == 1]["Amount"].sum()))
#     return dcc.Markdown("**{}**".format(won))


# # updates middle indicator value based on df updates
# @app.callback(
#     Output("middle_opportunities_indicator", "children"),
#     [Input("opportunities_df", "data")],
# )
# def middle_opportunities_indicator_callback(df):
#     df = pd.read_json(df, orient="split")
#     active = millify(str(df[(df["IsClosed"] == 0)]["Amount"].sum()))
#     return dcc.Markdown("**{}**".format(active))


# # updates right indicator value based on df updates
# @app.callback(
#     Output("right_opportunities_indicator", "children"),
#     [Input("opportunities_df", "data")],
# )
# def right_opportunities_indicator_callback(df):
#     df = pd.read_json(df, orient="split")
#     lost = millify(str(df[(df["IsWon"] == 0) & (df["IsClosed"] == 1)]["Amount"].sum()))
#     return dcc.Markdown("**{}**".format(lost))


# # hide/show modal
# @app.callback(
#     Output("opportunities_modal", "style"), [Input("new_opportunity", "n_clicks")]
# )
# def display_opportunities_modal_callback(n):
#     if n > 0:
#         return {"display": "block"}
#     return {"display": "none"}


# # reset to 0 add button n_clicks property
# @app.callback(
#     Output("new_opportunity", "n_clicks"),
#     [
#         Input("opportunities_modal_close", "n_clicks"),
#         Input("submit_new_opportunity", "n_clicks"),
#     ],
# )
# def close_modal_callback(n, n2):
#     return 0


# # add new opportunity to salesforce and stores new df in hidden div
# @app.callback(
#     Output("opportunities_df", "data"),
#     [Input("submit_new_opportunity", "n_clicks")],
#     [
#         State("new_opportunity_name", "value"),
#         State("new_opportunity_stage", "value"),
#         State("new_opportunity_amount", "value"),
#         State("new_opportunity_probability", "value"),
#         State("new_opportunity_date", "date"),
#         State("new_opportunity_type", "value"),
#         State("new_opportunity_source", "value"),
#         State("opportunities_df", "data"),
#     ],
# )
# def add_opportunity_callback(
#     n_clicks, name, stage, amount, probability, date, o_type, source, current_df
# ):
#     if n_clicks > 0:
#         if name == "":
#             name = "Not named yet"
#         query = {
#             "Name": name,
#             "StageName": stage,
#             "Amount": amount,
#             "Probability": probability,
#             "CloseDate": date,
#             "Type": o_type,
#             "LeadSource": source,
#         }

#         sf_manager.add_opportunity(query)

#         df = sf_manager.get_opportunities()

#         return df.to_json(orient="split")

#     return current_df


# # updates top open opportunities based on df updates
# @app.callback(
#     Output("top_open_opportunities", "children"), [Input("opportunities_df", "data")]
# )
# def top_open_opportunities_callback(df):
#     df = pd.read_json(df, orient="split")
#     return top_open_opportunities(df)


# # updates top lost opportunities based on df updates
# @app.callback(
#     Output("top_lost_opportunities", "children"), [Input("opportunities_df", "data")]
# )
# def top_lost_opportunities_callback(df):
#     df = pd.read_json(df, orient="split")
#     return top_lost_opportunities(df)