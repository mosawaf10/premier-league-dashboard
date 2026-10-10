
import pandas as pd
import plotly.express as px
import subprocess
import sys
from dash import Dash, dcc, html, Input, Output, dash_table, ctx



df = pd.read_csv("premier_league.csv")
scorers_df = pd.read_csv("top_scorers.csv")


app = Dash(__name__)

teams = sorted(df["Team"].dropna().unique())

app.layout = html.Div(
    style={"fontFamily": "Arial", "padding": "25px"},
    children=[
        html.H1(
            "Premier League Analytics Dashboard",
            style={"textAlign": "center"}
        ),
        dcc.Interval(
            id="refresh-interval",
            interval=3600 * 1000,
            n_intervals=0
        ),

        html.Label("Select a Team"),

        dcc.Dropdown(
            id="team-filter",
            options=[{"label": "All Teams", "value": "All"}]
            + [{"label": team, "value": team} for team in teams],
            value="All",
            clearable=False
        ),

        html.Div(
            id="kpi-cards",
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": "15px",
                "marginTop": "25px"
            }
        ),

        dcc.Graph(id="points-chart"),
        dcc.Graph(id="goals-chart"),

        html.H2("Top Scorers"),

        dash_table.DataTable(
            id="scorers-table",
            data=scorers_df[
                ["rank", "Name", "Goals", "Assists", "Played"]
            ].drop_duplicates(subset=["Name"]).to_dict("records"),
            columns=[
                {"name": "Rank", "id": "rank"},
                {"name": "Player", "id": "Name"},
                {"name": "Goals", "id": "Goals"},
                {"name": "Assists", "id": "Assists"},
                {"name": "Matches Played", "id": "Played"}
            ],
            page_size=10,
            sort_action="native",
            style_table={"overflowX": "auto"},
            style_cell={
                "textAlign": "left",
                "padding": "10px"
            },
            style_header={"fontWeight": "bold"}
        )
    ]
)



@app.callback(
    Output("kpi-cards", "children"),
    Output("points-chart", "figure"),
    Output("goals-chart", "figure"),
    Output("scorers-table", "data"),
    Input("team-filter", "value"),
    Input("refresh-interval", "n_intervals")
)
def update_dashboard(selected_team, n_intervals):
    global df, scorers_df

    if ctx.triggered_id == "refresh-interval":
        try:
            subprocess.run(
                [sys.executable, "scraper.py"],
                check=True,
                timeout=120
            )

            subprocess.run(
                [sys.executable, "top_scorers_scraper.py"],
                check=True,
                timeout=120
            )

            print("Data refreshed successfully!")

        except Exception as error:
            print("Data refresh failed:", error)

    df = pd.read_csv("premier_league.csv")
    scorers_df = pd.read_csv("top_scorers.csv")


    if selected_team == "All":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["Team"] == selected_team]

    total_teams = len(filtered_df)
    total_points = filtered_df["Points"].sum()
    total_goals = filtered_df["Goals For"].sum()
    avg_goals = (
        filtered_df["Goals For"].mean()
        if total_teams else 0
    )

    cards = [
        ("Teams", total_teams),
        ("Total Points", total_points),
        ("Total Goals", total_goals),
        ("Average Goals", round(avg_goals, 2))
    ]

    card_elements = [
        html.Div(
            [
                html.H3(title),
                html.H2(value)
            ],
            style={
                "backgroundColor": "#eaf2f8",
                "padding": "15px",
                "textAlign": "center",
                "borderRadius": "10px"
            }
        )
        for title, value in cards
    ]

    points_fig = px.bar(
        filtered_df.sort_values("Points", ascending=False),
        x="Team",
        y="Points",
        title="Points Comparison by Team"
    )

    goals_fig = px.bar(
        filtered_df.sort_values("Goals For", ascending=False),
        x="Team",
        y="Goals For",
        title="Goals Scored by Team"
    )

    scorer_data = scorers_df[
        ["rank", "Name", "Goals", "Assists", "Played"]
    ].drop_duplicates(subset=["Name"]).to_dict("records")

    return card_elements, points_fig, goals_fig, scorer_data


if __name__ == "__main__":
    app.run(debug=True)
