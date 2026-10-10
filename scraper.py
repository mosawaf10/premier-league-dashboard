
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.bbc.co.uk/sport/football/premier-league/table"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table")

if table is None:
    raise ValueError("No league table found on the page.")


headers = [
    th.get_text(" ", strip=True)
    for th in table.find_all("th")
]

rows = []

for tr in table.find_all("tr"):
    cells = tr.find_all("td")
    values = [cell.get_text(" ", strip=True) for cell in cells]

    if len(values) == len(headers):
        rows.append(values)

df = pd.DataFrame(rows, columns=headers)

df["Team"] = df["Team"].str.replace(
    r"^\d+\s*", "", regex=True
)

df.to_csv(
    "premier_league.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head())
print("\nCSV file saved successfully!")
print("Number of teams:", len(df))
print("Columns:", df.columns.tolist())
