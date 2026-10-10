
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.bbc.co.uk/sport/football/premier-league/top-scorers"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
)

response.raise_for_status()
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.find_all("table")

if not tables:
    raise ValueError("No tables found on the page.")

table = tables[0]

headers = [
    th.get_text(" ", strip=True)
    for th in table.find_all("th")
]

rows = []

for tr in table.find_all("tr"):
    cells = tr.find_all("td")
    values = [cell.get_text(" ", strip=True) for cell in cells]

    if headers and len(values) == len(headers):
        rows.append(values)

df = pd.DataFrame(rows, columns=headers)

# Remove duplicated text within player names
def clean_name(name):
    words = str(name).split()
    if len(words) % 2 == 0:
        middle = len(words) // 2
        if words[:middle] == words[middle:]:
            return " ".join(words[:middle])
    return name

df["Name"] = df["Name"].apply(clean_name)

# Keep only the columns needed for the dashboard
df = df[
    [
        "rank",
        "Name",
        "Goals",
        "Assists",
        "Played",
        "Total Shots",
        "Goal Conversion",
        "Shot Accuracy"
    ]
]

df = df.drop_duplicates()

if df.empty:
    raise ValueError("No scorer data extracted. Check the page structure.")

df.to_csv(
    "top_scorers.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head(10).to_string(index=False))
print("\nTop scorers CSV saved successfully!")
print("Number of rows:", len(df))
print("Columns:", df.columns.tolist())
