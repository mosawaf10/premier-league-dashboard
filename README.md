# Premier League Analytics Dashboard

## Project Overview

This project is an interactive dashboard for analyzing Premier League statistics. It displays league standings, team points, goals scored, and top scorers.

## Data Sources

- BBC Sport Premier League Table
- BBC Sport Premier League Top Scorers

## Features

- Web scraping using Python and BeautifulSoup.
- Saving scraped data into CSV files.
- Four KPI cards showing teams, total points, total goals, and average goals.
- Interactive charts for team points and goals scored.
- Team filter to explore individual teams.
- Top scorers table showing goals, assists, and matches played.
- Automatic data refresh every hour using Windows Task Scheduler.
- Batch script to update both CSV datasets automatically.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Plotly
- Dash
- Windows Task Scheduler

## Project Files

- `scraper.py`: Scrapes Premier League standings.
- `top_scorers_scraper.py`: Scrapes top scorers.
- `app.py`: Runs the interactive dashboard.
- `premier_league.csv`: League standings dataset.
- `top_scorers.csv`: Top scorers dataset.
- `refresh_data.bat`: Runs both scraping scripts to refresh the datasets.
- `check_data.py`: Checks the scraped data.

## How to Run

1. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4 pandas plotly dash lxml
   ```

2. Scrape the league standings:

   ```bash
   python scraper.py
   ```

3. Scrape the top scorers:

   ```bash
   python top_scorers_scraper.py
   ```

4. Run the dashboard:

   ```bash
   python app.py
   ```

5. Open the dashboard in your browser:

   http://127.0.0.1:8050/

## Automatic Data Refresh

The `refresh_data.bat` script runs both scraping scripts and updates the CSV files. Windows Task Scheduler is configured to run the batch script every hour. The computer must be running for the scheduled task to execute.

## Author

AI Engineering Student
