## Project Overview

This project is an interactive dashboard for analyzing Premier League statistics. It displays league standings, team points, goals scored, and top scorers using data collected from BBC Sport.

## Data Sources

- [BBC Sport Premier League Table](https://www.bbc.co.uk/sport/football/premier-league/table)
- [BBC Sport Premier League Top Scorers](https://www.bbc.co.uk/sport/football/premier-league/top-scorers)

## Features

- Web scraping using Python and BeautifulSoup.
- Saving scraped data into CSV files.
- Four KPI cards showing teams, total points, total goals, and average goals.
- Interactive charts for team points and goals scored.
- Team filter to explore individual teams.
- Top scorers table showing goals, assists, and matches played.
- Automatic data refresh every hour.
- Data quality checks for missing values and duplicate rows.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Plotly
- Dash

## Project Files

- `scraper.py`: Scrapes Premier League standings.
- `top_scorers_scraper.py`: Scrapes top scorers.
- `app.py`: Runs the interactive dashboard and handles automatic refresh.
- `check_data.py`: Checks dataset quality.
- `premier_league.csv`: League standings dataset.
- `top_scorers.csv`: Top scorers dataset.

## How to Run

1. Install the required libraries:

   `pip install requests beautifulsoup4 pandas plotly dash lxml`

2. Scrape the league standings:

   `python scraper.py`

3. Scrape the top scorers:

   `python top_scorers_scraper.py`

4. Run the dashboard:

   `python app.py`

5. Open `http://127.0.0.1:8050/` in your browser.

## Author

AI Engineering Student
